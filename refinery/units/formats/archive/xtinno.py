#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import annotations

import re

from refinery.units.formats.archive import ArchiveUnit

from refinery.lib.mime import FileMagicInfo as magic
from refinery.lib.json import BytesAsStringEncoder
from refinery.lib.inno.archive import InnoArchive, SetupFileFlags


class xtinno(ArchiveUnit):
    """
    Extract files from InnoSetup archives.
    """
    _STREAM_NAMES = 'meta/TSetup', 'meta/TData', 'embedded/uninstaller.exe'
    _ISCRIPT_NAME = 'embedded/script'
    _LICENSE_NAME = 'embedded/license.rtf'

    def unpack(self, data: bytearray):
        inno = InnoArchive(data, self)
        password = self.args.pwd or None

        if any(file.encrypted for file in inno.files) and password is None:
            self.log_info('some files are password-protected and no password was given')

        yield self._pack(self._STREAM_NAMES[0], None, inno.streams.TSetup.data)
        with BytesAsStringEncoder as encoder:
            yield self._pack(F'{self._STREAM_NAMES[0]}.json', None,
                encoder.dumps(inno.setup_info.json()).encode(self.codec))

        yield self._pack(self._STREAM_NAMES[1], None, inno.streams.TData.data)
        with BytesAsStringEncoder as encoder:
            yield self._pack(F'{self._STREAM_NAMES[1]}.json', None,
                encoder.dumps(inno.setup_data.json()).encode(self.codec))

        def _uninstaller(i=inno):
            return i.read_stream(i.streams.Uninstaller)
        yield self._pack(self._STREAM_NAMES[2], None, _uninstaller)

        if license := inno.setup_info.Header.get_license():
            yield self._pack(self._LICENSE_NAME, None, license.encode(self.codec))

        if script := inno.setup_info.Header.CompiledCode:
            yield self._pack(F'{self._ISCRIPT_NAME}.bin', None, script)
            yield self._pack(F'{self._ISCRIPT_NAME}.ps', None,
                lambda i=inno: i.ifps.disassembly().encode(self.codec))

        if dll := inno.setup_info.DecompressDLL:
            yield self._pack(F'embedded/decompress.{magic(dll).extension}', None, dll)

        if dll := inno.setup_info.DecryptionDLL:
            yield self._pack(F'embedded/decryption.{magic(dll).extension}', None, dll)

        for size, images in (
            ('small', inno.setup_info.WizardImagesSmall),
            ('large', inno.setup_info.WizardImagesLarge),
        ):
            _formatting = len(str(len(images) + 1))
            for k, img in enumerate(images, 1):
                yield self._pack(F'embedded/images/{size}{k:0{_formatting}d}.{magic(img).extension}', None, img)

        for file in inno.files:
            if file.dupe:
                continue
            yield self._pack(
                file.path,
                file.date,
                lambda i=inno, f=file: i.read_file_and_check(f, password=password),
                tags=[t.name for t in SetupFileFlags if t & file.tags],
            )

    @classmethod
    def handles(self, data):
        if data[:2] != B'MZ':
            return False
        if re.search(re.escape(InnoArchive.ChunkPrefix), data) is None:
            return False
        return bool(
            re.search(BR'Inno Setup Setup Data \(\d+\.\d+\.', data))
