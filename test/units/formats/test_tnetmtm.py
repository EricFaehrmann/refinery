#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from .. import TestUnitBase


class TestTnetmtmUnit(TestUnitBase):
    def test_content(self):
        unit = self.load()
        payload = unit(self.EXAMPLE_COM)
        self.assertTrue(b'<title>Example Domain</title>' in payload)

    def test_listHeaders(self):
        unit = self.load(list_header_names=True)
        headers = unit(self.EXAMPLE_COM).decode('utf-8').splitlines()
        self.assertSetEqual(set(headers), {
            'User-Agent', 'Accept', 'Accept-Encoding', 'Host', 'Connection', 'Age', 'Cache-Control', 'Content-Type',
            'Date', 'Etag', 'Expires', 'Last-Modified', 'Server', 'Vary', 'X-Cache', 'Content-Length'
        })

    def test_headerValue(self):
        unit = self.load(header_filter='User-Agent')
        user_agent = unit(self.EXAMPLE_COM).decode('utf-8').splitlines()
        self.assertEqual(user_agent, ['Wget/1.20.3 (msys)'])

    EXAMPLE_COM = bytes.fromhex(
        '373930363A343A747970653B343A687474703B373A76657273696F6E3B323A313823393A776562736F636B65743B303A7E3'
        '83A726573706F6E73653B313833373A363A726561736F6E3B323A4F4B2C31313A7374617475735F636F64653B333A323030'
        '2331333A74696D657374616D705F656E643B31383A313638323834363239312E313435373830335E31353A74696D6573746'
        '16D705F73746172743B31383A313638323834363239312E313434373837335E383A747261696C6572733B303A7E373A636F'
        '6E74656E743B313235363A3C21646F63747970652068746D6C3E0A3C68746D6C3E0A3C686561643E0A202020203C7469746'
        'C653E4578616D706C6520446F6D61696E3C2F7469746C653E0A0A202020203C6D65746120636861727365743D227574662D'
        '3822202F3E0A202020203C6D65746120687474702D65717569763D22436F6E74656E742D747970652220636F6E74656E743'
        'D22746578742F68746D6C3B20636861727365743D7574662D3822202F3E0A202020203C6D657461206E616D653D22766965'
        '77706F72742220636F6E74656E743D2277696474683D6465766963652D77696474682C20696E697469616C2D7363616C653'
        'D3122202F3E0A202020203C7374796C6520747970653D22746578742F637373223E0A20202020626F6479207B0A20202020'
        '202020206261636B67726F756E642D636F6C6F723A20236630663066323B0A20202020202020206D617267696E3A20303B0'
        'A202020202020202070616464696E673A20303B0A2020202020202020666F6E742D66616D696C793A202D6170706C652D73'
        '797374656D2C2073797374656D2D75692C20426C696E6B4D616353797374656D466F6E742C20225365676F65205549222C2'
        '0224F70656E2053616E73222C202248656C766574696361204E657565222C2048656C7665746963612C20417269616C2C20'
        '73616E732D73657269663B0A20202020202020200A202020207D0A20202020646976207B0A2020202020202020776964746'
        '83A2036303070783B0A20202020202020206D617267696E3A2035656D206175746F3B0A202020202020202070616464696E'
        '673A2032656D3B0A20202020202020206261636B67726F756E642D636F6C6F723A20236664666466663B0A2020202020202'
        '020626F726465722D7261646975733A20302E35656D3B0A2020202020202020626F782D736861646F773A20327078203370'
        '782037707820327078207267626128302C302C302C302E3032293B0A202020207D0A20202020613A6C696E6B2C20613A766'
        '97369746564207B0A2020202020202020636F6C6F723A20233338343838663B0A2020202020202020746578742D6465636F'
        '726174696F6E3A206E6F6E653B0A202020207D0A20202020406D6564696120286D61782D77696474683A203730307078292'
        '07B0A2020202020202020646976207B0A2020202020202020202020206D617267696E3A2030206175746F3B0A2020202020'
        '2020202020202077696474683A206175746F3B0A20202020202020207D0A202020207D0A202020203C2F7374796C653E202'
        '020200A3C2F686561643E0A0A3C626F64793E0A3C6469763E0A202020203C68313E4578616D706C6520446F6D61696E3C2F'
        '68313E0A202020203C703E5468697320646F6D61696E20697320666F722075736520696E20696C6C7573747261746976652'
        '06578616D706C657320696E20646F63756D656E74732E20596F75206D61792075736520746869730A20202020646F6D6169'
        '6E20696E206C69746572617475726520776974686F7574207072696F7220636F6F7264696E6174696F6E206F722061736B6'
        '96E6720666F72207065726D697373696F6E2E3C2F703E0A202020203C703E3C6120687265663D2268747470733A2F2F7777'
        '772E69616E612E6F72672F646F6D61696E732F6578616D706C65223E4D6F726520696E666F726D6174696F6E2E2E2E3C2F6'
        '13E3C2F703E0A3C2F6469763E0A3C2F626F64793E0A3C2F68746D6C3E0A2C373A686561646572733B3339343A31353A333A'
        '4167652C363A3432323338372C5D33353A31333A43616368652D436F6E74726F6C2C31343A6D61782D6167653D363034383'
        '0302C5D34343A31323A436F6E74656E742D547970652C32343A746578742F68746D6C3B20636861727365743D5554462D38'
        '2C5D34303A343A446174652C32393A53756E2C2033302041707220323032332030393A31383A313220474D542C5D32393A3'
        '43A457461672C31383A22333134373532363934372B6964656E74222C5D34333A373A457870697265732C32393A53756E2C'
        '203037204D617920323032332030393A31383A313220474D542C5D35303A31333A4C6173742D4D6F6469666965642C32393'
        'A5468752C203137204F637420323031392030373A31383A323620474D542C5D32373A363A5365727665722C31343A454353'
        '20286273612F45423138292C5D32363A343A566172792C31353A4163636570742D456E636F64696E672C5D31363A373A582'
        'D43616368652C333A4849542C5D32353A31343A436F6E74656E742D4C656E6774682C343A313235362C5D5D31323A687474'
        '705F76657273696F6E3B383A485454502F312E312C7D373A726571756573743B3339313A343A706174683B313A2F2C393A6'
        '17574686F726974793B303A2C363A736368656D653B353A68747470732C363A6D6574686F643B333A4745542C343A706F72'
        '743B333A34343323343A686F73743B31313A6578616D706C652E636F6D3B31333A74696D657374616D705F656E643B31373'
        'A313638323834363239302E3937343137385E31353A74696D657374616D705F73746172743B31373A313638323834363239'
        '302E3937343137385E383A747261696C6572733B303A7E373A636F6E74656E743B303A2C373A686561646572733B3135313'
        'A33363A31303A557365722D4167656E742C31383A576765742F312E32302E3320286D737973292C5D31353A363A41636365'
        '70742C333A2A2F2A2C5D33303A31353A4163636570742D456E636F64696E672C383A6964656E746974792C5D32323A343A4'
        '86F73742C31313A6578616D706C652E636F6D2C5D32383A31303A436F6E6E656374696F6E2C31303A4B6565702D416C6976'
        '652C5D5D31323A687474705F76657273696F6E3B383A485454502F312E312C7D31373A74696D657374616D705F637265617'
        '465643B31373A313638323834363239302E3937343137385E373A636F6D6D656E743B303A3B383A6D657461646174613B30'
        '3A7D363A6D61726B65643B303A3B393A69735F7265706C61793B303A7E31313A696E7465726365707465643B353A66616C7'
        '3652131313A7365727665725F636F6E6E3B343932343A343A766961323B303A7E31313A6369706865725F6C6973743B303A'
        '5D31313A6369706865725F6E616D653B32323A544C535F4145535F3235365F47434D5F5348413338343B31313A616C706E5'
        'F6F66666572733B303A5D31363A63657274696669636174655F6C6973743B343330353A323538393A2D2D2D2D2D42454749'
        '4E2043455254494649434154452D2D2D2D2D0A4D494948536A4343426A4B67417749424167495144422F4C47455559782B4'
        'F475A30456A6257747A3854414E42676B71686B69473977304241517346414442500A4D517377435159445651514745774A'
        '56557A45564D424D474131554543684D4D52476C6E61554E6C636E51675357356A4D536B774A77594456515144457942450'
        'A61576470513256796443425554464D67556C4E4249464E49515449314E6941794D44497749454E424D544165467730794D'
        '7A41784D544D774D4441774D4442610A467730794E4441794D544D794D7A55354E546C614D4947574D51737743515944565'
        '1514745774A56557A45544D4245474131554543424D4B5132467361575A760A636D3570595445554D424947413155454278'
        '4D4C5447397A494546755A3256735A584D78516A424142674E5642416F4D4F556C7564475679626D5630777142440A62334'
        'A7762334A6864476C7662734B675A6D39797771424263334E705A32356C5A4D4B67546D46745A5850436F4746755A4D4B67'
        '546E5674596D5679637A45590A4D4259474131554541784D50643364334C6D5634595731776247557562334A6E4D4949424'
        '96A414E42676B71686B6947397730424151454641414F43415138410A4D49494243674B4341514541776F423369566D3452'
        '572B3653746B522B6E757478316651657675322B74304675364B42636276686679485358793777306E4A4F0A645454346A5'
        '74C6A537470526B4E5142505A774D7748483335692B323167646E4A7444652F78664F384958394D63466D796F646C425563'
        '715838437275497A440A7639415866324F6A585042472B3461712B3033584B6C352F6D7541546C33322B2B3330315677316'
        '4586F47594E656F5751714C5473485433575333744F4F662B0A6568757A4E755A2B726A2B6570686144336C4D42546F4541'
        '72727443395239314B54544E365953414F4B34384E7854413843664F4D464B3569747866497142350A2B45394F535154696'
        '45879714C796F65412B7878544B4D7159667876797045656B316F7565416859397536374E4342646D756176787466797677'
        '70372B6F36530A642B4E7365777841686D524B4665787731334B4F597A4468432B39614D4A63754A514944415141426F344'
        '9443244434341395177487759445652306A424267770A466F41557432756936716971684978353672546144356979785A56'
        '3275665177485159445652304F42425945464C4354502B675867763173737259586838766A0A675036436D7747654D49474'
        '242674E5648524545656A423467673933643363755A586868625842735A533576636D654343325634595731776247557562'
        '6D56300A6767746C654746746347786C4C6D566B6459494C5A586868625842735A53356A623232434332563459573177624'
        '7557562334A6E67673933643363755A5868680A625842735A53356A62323243443364336479356C654746746347786C4C6D'
        '566B64594950643364334C6D56345957317762475575626D56304D413447413155640A447745422F775145417749466F444'
        '16442674E5648535545466A4155426767724267454642516344415159494B77594242515548417749776759384741315564'
        '0A48775342687A4342684442416F443667504959366148523063446F764C324E7962444D755A476C6E61574E6C636E51755'
        '93239744C3052705A326C445A584A300A56457854556C4E42553068424D6A55324D6A41794D454E424D5330304C6D4E7962'
        '4442416F443667504959366148523063446F764C324E79624451755A476C6E0A61574E6C636E5175593239744C3052705A3'
        '26C445A584A3056457854556C4E42553068424D6A55324D6A41794D454E424D5330304C6D4E796244412B42674E560A4853'
        '41454E7A41314D444D47426D654244414543416A41704D4363474343734741515546427749424668746F644852774F69387'
        '6643364334C6D52705A326C6A0A5A584A304C6D4E766253394455464D77667759494B7759424251554841514545637A4278'
        '4D4351474343734741515546427A41426868686F644852774F6938760A62324E7A6343356B61576470593256796443356A6'
        '2323077535159494B775942425155484D414B4750576830644841364C79396A59574E6C636E527A4C6D52700A5A326C6A5A'
        '584A304C6D4E766253394561576470513256796446524D55314A5451564E49515449314E6A49774D6A4244515445744D533'
        '56A636E5177435159440A565230544241497741444343415838474369734741515142316E6B434241494567674676424949'
        '426177467041485941377333515A4E586247733746584C65640A744D30546F6A4B48526E7938374E37445555685A526E456'
        '6745A734141414746713067464977414142414D41527A42464169454171742B664B366A46644741360A7476304557743972'
        '61783057594256347265396A675A6771307A6934325155434945426831794B70507667583142726545307742556D72694F5'
        '655684A5337370A4B67463139336654323837374148634163396D656952744D6C6E6967494831486E65617978687A515556'
        '35784753714D613441516573463363725541414147460A713067466E77414142414D41534442474169454131325355464B3'
        '572674C71527A76676372375A7A56346E6C2B5A74396C6C6F417A524C6650633776535041430A4951435850627753637831'
        '72452B426A4661775A6C566A4C6A2F3150734D304B515163736648445A4A55544C774142324145697734327661706B63304'
        '42B56710A417671644D4F73635567484C5674307367646D37763673353249527A4141414268617449425634414141514441'
        '45637752514968414E3562684874686F79574D0A4A334351422F3169594645684D6755566B466848444D2F6E6C453954684'
        '377684169415076504A5879703761326B7A774A5833503766714835586B6F337250680A437A526F58596436572B516B436A'
        '414E42676B71686B6947397730424151734641414F43415145415765524B324B6D437570704B38574D4D6258596D64624D3'
        '80A644C3746397A326E6B5A4C347A7759745742447438376A572F477A2F453559797A552F70687953464333536977765950'
        '396166596658614B72756E4A574374750A41472B357A53547578454C46544261466E5452684F534F2F786F3656795953707'
        '375564244305234313557357A396C30763168503578622F664541777847784F0A496B334C673263366B3738727863576347'
        '764A446F535537685062335532366F68613765464853524D41594E386766557841693651325446346A2F61724D56420A723'
        '6513336454A3264506354753070394E6C6D426D38644533346C7A75544E433647444354574664456C6F5139752F2F4D346B'
        '55554F6A576E386135584373310A32363374335461324A664B56697178705035722B477667564B47337147467243306D495'
        '97230423474667065435939542B637A34493647444D53503078673D3D0A2D2D2D2D2D454E44204345525449464943415445'
        '2D2D2D2D2D0A2C313730343A2D2D2D2D2D424547494E2043455254494649434154452D2D2D2D2D0A4D494945766A4343413'
        '66167417749424167495142746A5A424E56595130623269692B6E56434A2B7844414E42676B71686B694739773042415173'
        '46414442680A4D517377435159445651514745774A56557A45564D424D474131554543684D4D52476C6E61554E6C636E516'
        '75357356A4D526B77467759445651514C457842330A643363755A476C6E61574E6C636E5175593239744D53417748675944'
        '56515144457864456157647051325679644342486247396959577767556D3976644342440A51544165467730794D5441304'
        'D5451774D4441774D4442614677307A4D5441304D544D794D7A55354E546C614D453878437A414A42674E5642415954416C'
        '56540A4D525577457759445651514B4577784561576470513256796443424A626D4D784B54416E42674E5642414D5449455'
        '2705A326C445A584A304946524D557942530A55304567553068424D6A5532494449774D6A4167513045784D494942496A41'
        '4E42676B71686B6947397730424151454641414F43415138414D49494243674B430A415145417755757A5A556477764E315'
        '0574E76736E4F33445A7555664D524E557255706D526838734375786B422B5575334E793543694474332B5045304A36610A'
        '71586F64676F6A6C4556626248703959776C486E4C44514E4C744B533456624C38586C66733775487969554465357053515'
        '759515945395845306E773644646E0A67392F6E3030746E54434A527074384F6D524474563146304A754A39783870694C68'
        '4D6266794F494A564E7677545259414975452F2F692B7031684A496E75570A72614B496D7857386F487A663656476F31624'
        '4744E2B493274494A4C5972564A6D757A485A39626A5076586A31684A655250472F63554A3957495144674C47420A416672'
        '35796A4B377449346E687966464B335455714E615833734E6B2B63724F55364A57764867586A6B6B444B61373753552B6B4'
        '6626E4F386C775A563231720A656163726F6963674537585150554454495441486B2B715A39514944415141426F34494267'
        '6A43434158347745675944565230544151482F42416777426745420A2F7749424144416442674E564851344546675155743'
        '2756936716971684978353672546144356979785A563275665177487759445652306A42426777466F41550A413935514E56'
        '6252544C746D384B5069477876446C3749393056557744675944565230504151482F42415144416747474D4230474131556'
        '44A5151574D4251470A434373474151554642774D42426767724267454642516344416A4232426767724267454642516342'
        '415152714D4767774A4159494B775942425155484D4147470A47476830644841364C79397659334E774C6D52705A326C6A5'
        'A584A304C6D4E7662544241426767724267454642516377416F59306148523063446F764C324E680A5932567964484D755A'
        '476C6E61574E6C636E5175593239744C3052705A326C445A584A3052327876596D4673556D397664454E424C6D4E7964444'
        '24342674E560A485238454F7A41354D4465674E61417A686A466F644852774F69387659334A734D79356B61576470593256'
        '796443356A6232307652476C6E61554E6C636E52480A6247396959577853623239305130457559334A734D4430474131556'
        '4494151324D4451774377594A59495A4941596239624149424D41634742576542444145420A4D416747426D654244414543'
        '4154414942675A6E6751774241674977434159475A34454D415149444D41304743537147534962334451454243775541413'
        '449420A415143414D733565433931755767304B722B4857684D76416A767146634F336158624D4D39797431515036464376'
        '727A4D5869336345736169566936674C337A0A617833706673384C756C696357645351302F31732F64435962626478676C7'
        '6506251746143644237337352443243716B337035424A6C2B376A356E4C336137680A71472B66682F353074783862494B75'
        '78543862315A3131646D7A7A702F326E3359577A57326650394E73617241346832306B73756459626A2F4E6856665362430'
        'A4558666650674B3266504F72653371474E6D2B343939695463632B4733334D772B6E75723753705A79454B454F78455847'
        '6C4C7A7951345566614A62636D65360A636531585232624675414A4B5A5452656939417150434363555A6C4D35314B65393'
        '273524B7732536668336F69757332466B4F483669706A7633552F363937450A4137734B50506377372B75765450794C4E68'
        '427A50764F6B0A2D2D2D2D2D454E442043455254494649434154452D2D2D2D2D0A2C5D333A746C733B343A7472756521353'
        'A6572726F723B303A7E353A73746174653B313A3323333A7669613B303A7E31313A746C735F76657273696F6E3B373A544C'
        '5376312E333B31353A746C735F65737461626C69736865643B343A747275652131393A74696D657374616D705F746C735F7'
        '3657475703B31383A313638323834363239302E393732313633375E31393A74696D657374616D705F7463705F7365747570'
        '3B31383A313638323834363239302E323431363339315E31353A74696D657374616D705F73746172743B31383A313638323'
        '834363239302E313239343139385E31333A74696D657374616D705F656E643B303A7E31343A736F757263655F6164647265'
        '73733B35363A33363A323030313A346464373A656538303A303A393036663A363861313A333665333A356333373B353A343'
        '233383523313A3023313A30235D333A736E693B31313A6578616D706C652E636F6D3B31303A69705F616464726573733B35'
        '323A33343A323630363A323830303A3232303A313A3234383A313839333A323563383A313934363B333A34343323313A302'
        '3313A30235D323A69643B33363A31643037666333352D343565622D343530642D396666662D343433373631633032353662'
        '3B343A616C706E3B303A2C373A616464726573733B32313A31313A6578616D706C652E636F6D3B333A343433235D7D31313'
        'A636C69656E745F636F6E6E3B3436323A31303A70726F78795F6D6F64653B32373A726576657273653A68747470733A2F2F'
        '6578616D706C652E636F6D3B31313A6369706865725F6C6973743B303A5D31313A616C706E5F6F66666572733B303A5D313'
        '63A63657274696669636174655F6C6973743B303A5D333A746C733B353A66616C736521353A6572726F723B303A7E383A73'
        '6F636B6E616D653B32313A333A3A3A313B343A3830383023313A3023313A30235D353A73746174653B313A332331313A746'
        'C735F76657273696F6E3B303A7E31343A746C735F657874656E73696F6E733B303A5D31353A746C735F65737461626C6973'
        '6865643B353A66616C73652131393A74696D657374616D705F746C735F73657475703B303A7E31353A74696D657374616D7'
        '05F73746172743B31383A313638323834363239302E313238343530395E31333A74696D657374616D705F656E643B303A7E'
        '333A736E693B303A7E383A6D69746D636572743B303A7E323A69643B33363A36363531336164612D353433382D346239322'
        'D386663662D3864373863643361343735613B31313A6369706865725F6E616D653B303A7E343A616C706E3B303A7E373A61'
        '6464726573733B32323A333A3A3A313B353A343233383423313A3023313A30235D7D353A6572726F723B303A7E323A69643'
        'B33363A30313531393164372D376566392D346338312D393331612D3265313839353634333737363B7D'
    )