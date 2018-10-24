import pytest
import os
import json

from patent_client.epo_ops import Epo, Inpadoc

FIXTURES = os.path.join(os.path.dirname(__file__), "fixtures")


class TestInpadoc:
    def test_can_get_epo_pub(self):
        pub = Inpadoc.objects.get("CA2944968")
        assert pub.title == "WIRELINE POWER SUPPLY DURING ELECTRIC POWERED FRACTURING OPERATIONS"
        assert pub.publication == 'CA2944968A1'
        assert pub.applicants == ["US WELL SERVICES LLC"]
        assert pub.inventors == ["OEHRING, JARED, ", "HINDERLITER, BRANDON"]
        assert len(pub.full_text.description) == 35306
        assert pub.full_text.claims[:5] == [
            "1. A fracturing system comprising: a turbine generator having an electrical output; an electric motor that is in electrical communication with the electrical output; a fracturing pump that is driven by the electric motor; and a wireline system that is in electrical communication with the electrical output.",
            "2. The system of claim 1, further comprising a variable frequency drive connected to the electric motor to control the speed of the motor, wherein the variable frequency drive frequently performs electric motor diagnostics to prevent damage to the at least one electric motor.",
            "3. The system of claim 1, wherein the wireline system comprises a wireline tool that is disposable in a wellbore that is selected from the group consisting of a perforating gun, a plug, a formation logging tool, a cutting tool, a casing imaging tool, and combinations thereof.",
            "4. The system of claim 1, further comprising trailers that contain at least one power distribution panel that supplies power to the hydraulic fracturing equipment.",
            "5. The system of claim 4, where the trailers further contain receptacles for attaching cable to the hydraulic fracturing equipment and cables that can sustain the power draw of the turbines with three separate plugs for the three phase power.",
        ]
        assert pub.images.url == "http://ops.epo.org/rest-services/published-data/images/CA/2944968/A1/fullimage.pdf"
        assert pub.images.num_pages == 29
        assert pub.images.sections == {"ABSTRACT": 1, "CLAIMS": 22, "DESCRIPTION": 2, "DRAWINGS": 25}

    def test_can_download_full_images(self, tmpdir):
        pub = Inpadoc.objects.get("CA2944968")
        pub.images.download(path=str(tmpdir))
        assert os.listdir(str(tmpdir)) == ["CA2944968.pdf"]

    def test_can_handle_russian_cases(self):
        pub = Inpadoc.objects.get("RU2015124071")
        assert pub.title == "БУРОВОЕ ДОЛОТО ДЛЯ БУРИЛЬНОГО УСТРОЙСТВА"
        assert pub.cpc_class ==  [
                "E21B 7/064",
                "E21B 17/04",
                "E21B 47/01",
                "E21B 47/12",
                "E21B 7/067",
                "E21B 10/08",
                "E21B 10/567",
            ]
        assert pub.priority_claims == ["13/683,540", "US 2013/066560"]

    def test_can_get_ep_application(self):
        pubs = Inpadoc.objects.filter(application="EP13844704")
        assert len(pubs) == 1
        assert pubs[0].title == 'ATTITUDE REFERENCE FOR TIEBACK/OVERLAP PROCESSING'

    def test_pct(self):
        doc = Inpadoc.objects.get("PCT/US16/15853")
        assert doc.title == 'DUAL MODE TELEMETRY'

    @pytest.mark.skip("doesn't work")
    def test_can_get_us_application(self):
        pub = Inpadoc.objects.get(application="US15915966")
        assert pub.title  == "DEVICE AND METHOD FOR SURVEYING BOREHOLES OR ORIENTING DOWNHOLE ASSEMBLIES"


    def test_can_get_inpadoc_family(self):
        family = Inpadoc.objects.filter(application="EP13844704")[0].family
        cases = [m.publication for m in family]
        assert cases == [
            "EP2906782A2",
            "EP2906782A4",
            "CA2887530A1",
            "CN104968889A",
            "RU2015117646A",
            "US2014102795A1",
            "US9291047B2",
            "US2016245070A1",
            "US10047600B2",
            "WO2014059282A2",
            "WO2014059282A3",
        ]

    def test_can_get_legal_status(self):
        pub = Inpadoc.objects.get("CA2300029C")
        print(pub.legal)
        assert pub.legal == [
            {
                "description": "EXAMINATION REQUEST",
                "explanation": "+",
                "code": "EEER",
                "date": "2005-02-03",
            }
        ]

    def test_can_search_inpadoc(self):
        results = Inpadoc.objects.filter(applicant="Scientific Drilling")
        assert len(results) == 206
        assert results.values('title')[:10] == [{'title': 'SUB-SURFACE ELECTROMAGNETIC TELEMETRY SYSTEMS AND METHODS'},
 {'title': 'DEVICE AND METHOD FOR SURVEYING BOREHOLES OR ORIENTING DOWNHOLE '
           'ASSEMBLIES'},
 {'title': 'DEVICE AND METHOD FOR SURVEYING BOREHOLES OR ORIENTING DOWNHOLE '
           'ASSEMBLIES'},
 {'title': 'METHOD FOR IMPROVING SURVEY MEASUREMENT DENSITY ALONG A BOREHOLE'},
 {'title': 'LOGGING-WHILE-DRILLING SPECTRAL AND AZIMUTHAL GAMMA RAY APPARATUS '
           'AND METHODS'},
 {'title': 'DOWNHOLE MWD SIGNAL ENHANCEMENT, TRACKING, AND DECODING'},
 {'title': 'LOGGING-WHILE-DRILLING SPECTRAL AND AZIMUTHAL GAMMA RAY APPARATUS '
           'AND METHODS'},
 {'title': 'TUMBLE GYRO SURVEYOR'},
 {'title': 'SURFACE COIL FOR WELLBORE POSITIONING'},
 {'title': 'COHERENT MEASUREMENT METHOD FOR DOWNHOLE APPLICATIONS'}]
        #us_cases = results.filter(publication__country='US')[:5]
        #from pprint import pprint
        #pprint(us_cases)
        #assert False


class TestEpoRegister:
    def test_can_get_epo_data(self):
        pub = Epo.objects.get("EP3221665A1")
        assert pub.status[0] == {'code': '15', 'date': '20170825', 'description': 'Request for examination was made'}
        assert pub.title == 'INERTIAL CAROUSEL POSITIONING'
        assert pub.procedural_steps[0] == {'code': 'RFEE', 'date': '20171113', 'description': 'Renewal fee payment - 03', 'phase': 'undefined'}