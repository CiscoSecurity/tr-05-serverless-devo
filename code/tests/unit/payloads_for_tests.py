EXPECTED_RESPONSE_OF_JWKS_ENDPOINT = {
    'keys': [
        {
            'kty': 'RSA',
            'n': 'tSKfSeI0fukRIX38AHlKB1YPpX8PUYN2JdvfM-XjNmLfU1M74N0V'
                 'mdzIX95sneQGO9kC2xMIE-AIlt52Yf_KgBZggAlS9Y0Vx8DsSL2H'
                 'vOjguAdXir3vYLvAyyHin_mUisJOqccFKChHKjnk0uXy_38-1r17'
                 '_cYTp76brKpU1I4kM20M__dbvLBWjfzyw9ehufr74aVwr-0xJfsB'
                 'Vr2oaQFww_XHGz69Q7yHK6DbxYO4w4q2sIfcC4pT8XTPHo4JZ2M7'
                 '33Ea8a7HxtZS563_mhhRZLU5aynQpwaVv2U--CL6EvGt8TlNZOke'
                 'Rv8wz-Rt8B70jzoRpVK36rR-pHKlXhMGT619v82LneTdsqA25Wi2'
                 'Ld_c0niuul24A6-aaj2u9SWbxA9LmVtFntvNbRaHXE1SLpLPoIp8'
                 'uppGF02Nz2v3ld8gCnTTWfq_BQ80Qy8e0coRRABECZrjIMzHEg6M'
                 'loRDy4na0pRQv61VogqRKDU2r3_VezFPQDb3ciYsZjWBr3HpNOkU'
                 'jTrvLmFyOE9Q5R_qQGmc6BYtfk5rn7iIfXlkJAZHXhBy-ElBuiBM'
                 '-YSkFM7dH92sSIoZ05V4MP09Xcppx7kdwsJy72Sust9Hnd9B7V35'
                 'YnVF6W791lVHnenhCJOziRmkH4xLLbPkaST2Ks3IHH7tVltM6NsR'
                 'k3jNdVM',
            'e': 'AQAB',
            'alg': 'RS256',
            'kid': '02B1174234C29F8EFB69911438F597FF3FFEE6B7',
            'use': 'sig'
        }
    ]
}

RESPONSE_OF_JWKS_ENDPOINT_WITH_WRONG_KEY = {
    'keys': [
        {
            'kty': 'RSA',
            'n': 'pSKfSeI0fukRIX38AHlKB1YPpX8PUYN2JdvfM-XjNmLfU1M74N0V'
                 'mdzIX95sneQGO9kC2xMIE-AIlt52Yf_KgBZggAlS9Y0Vx8DsSL2H'
                 'vOjguAdXir3vYLvAyyHin_mUisJOqccFKChHKjnk0uXy_38-1r17'
                 '_cYTp76brKpU1I4kM20M__dbvLBWjfzyw9ehufr74aVwr-0xJfsB'
                 'Vr2oaQFww_XHGz69Q7yHK6DbxYO4w4q2sIfcC4pT8XTPHo4JZ2M7'
                 '33Ea8a7HxtZS563_mhhRZLU5aynQpwaVv2U--CL6EvGt8TlNZOke'
                 'Rv8wz-Rt8B70jzoRpVK36rR-pHKlXhMGT619v82LneTdsqA25Wi2'
                 'Ld_c0niuul24A6-aaj2u9SWbxA9LmVtFntvNbRaHXE1SLpLPoIp8'
                 'uppGF02Nz2v3ld8gCnTTWfq_BQ80Qy8e0coRRABECZrjIMzHEg6M'
                 'loRDy4na0pRQv61VogqRKDU2r3_VezFPQDb3ciYsZjWBr3HpNOkU'
                 'jTrvLmFyOE9Q5R_qQGmc6BYtfk5rn7iIfXlkJAZHXhBy-ElBuiBM'
                 '-YSkFM7dH92sSIoZ05V4MP09Xcppx7kdwsJy72Sust9Hnd9B7V35'
                 'YnVF6W791lVHnenhCJOziRmkH4xLLbPkaST2Ks3IHH7tVltM6NsR'
                 'k3jNdVM',
            'e': 'AQAB',
            'alg': 'RS256',
            'kid': '02B1174234C29F8EFB69911438F597FF3FFEE6B7',
            'use': 'sig'
        }
    ]
}

PRIVATE_KEY = """-----BEGIN RSA PRIVATE KEY-----
MIIJKwIBAAKCAgEAtSKfSeI0fukRIX38AHlKB1YPpX8PUYN2JdvfM+XjNmLfU1M7
4N0VmdzIX95sneQGO9kC2xMIE+AIlt52Yf/KgBZggAlS9Y0Vx8DsSL2HvOjguAdX
ir3vYLvAyyHin/mUisJOqccFKChHKjnk0uXy/38+1r17/cYTp76brKpU1I4kM20M
//dbvLBWjfzyw9ehufr74aVwr+0xJfsBVr2oaQFww/XHGz69Q7yHK6DbxYO4w4q2
sIfcC4pT8XTPHo4JZ2M733Ea8a7HxtZS563/mhhRZLU5aynQpwaVv2U++CL6EvGt
8TlNZOkeRv8wz+Rt8B70jzoRpVK36rR+pHKlXhMGT619v82LneTdsqA25Wi2Ld/c
0niuul24A6+aaj2u9SWbxA9LmVtFntvNbRaHXE1SLpLPoIp8uppGF02Nz2v3ld8g
CnTTWfq/BQ80Qy8e0coRRABECZrjIMzHEg6MloRDy4na0pRQv61VogqRKDU2r3/V
ezFPQDb3ciYsZjWBr3HpNOkUjTrvLmFyOE9Q5R/qQGmc6BYtfk5rn7iIfXlkJAZH
XhBy+ElBuiBM+YSkFM7dH92sSIoZ05V4MP09Xcppx7kdwsJy72Sust9Hnd9B7V35
YnVF6W791lVHnenhCJOziRmkH4xLLbPkaST2Ks3IHH7tVltM6NsRk3jNdVMCAwEA
AQKCAgEArx+0JXigDHtFZr4pYEPjwMgCBJ2dr8+L8PptB/4g+LoK9MKqR7M4aTO+
PoILPXPyWvZq/meeDakyZLrcdc8ad1ArKF7baDBpeGEbkRA9JfV5HjNq/ea4gyvD
MCGou8ZPSQCnkRmr8LFQbJDgnM5Za5AYrwEv2aEh67IrTHq53W83rMioIumCNiG+
7TQ7egEGiYsQ745GLrECLZhKKRTgt/T+k1cSk1LLJawme5XgJUw+3D9GddJEepvY
oL+wZ/gnO2ADyPnPdQ7oc2NPcFMXpmIQf29+/g7FflatfQhkIv+eC6bB51DhdMi1
zyp2hOhzKg6jn74ixVX+Hts2/cMiAPu0NaWmU9n8g7HmXWc4+uSO/fssGjI3DLYK
d5xnhrq4a3ZO5oJLeMO9U71+Ykctg23PTHwNAGrsPYdjGcBnJEdtbXa31agI5PAG
6rgGUY3iSoWqHLgBTxrX04TWVvLQi8wbxh7BEF0yasOeZKxdE2IWYg75zGsjluyH
lOnpRa5lSf6KZ6thh9eczFHYtS4DvYBcZ9hZW/g87ie28SkBFxxl0brYt9uKNYJv
uajVG8kT80AC7Wzg2q7Wmnoww3JNJUbNths5dqKyUSlMFMIB/vOePFHLrA6qDfAn
sQHgUb9WHhUrYsH20XKpqR2OjmWU05bV4pSMW/JwG37o+px1yKECggEBANnwx0d7
ksEMvJjeN5plDy3eMLifBI+6SL/o5TXDoFM6rJxF+0UP70uouYJq2dI+DCSA6c/E
sn7WAOirY177adKcBV8biwAtmKHnFnCs/kwAZq8lMvQPtNPJ/vq2n40kO48h8fxb
eGcmyAqFPZ4YKSxrPA4cdbHIuFSt9WyaUcVFmzdTFHVlRP70EXdmXHt84byWNB4C
Heq8zmrNxPNAi65nEkUks7iBQMtuvyV2+aXjDOTBMCd66IhIh2iZq1O7kXUwgh1O
H9hCa7oriHyAdgkKdKCWocmbPPENOETgjraA9wRIXwOYTDb1X5hMvi1mCHo8xjMj
u4szD03xJVi7WrsCggEBANTEblCkxEyhJqaMZF3U3df2Yr/ZtHqsrTr4lwB/MOKk
zmuSrROxheEkKIsxbiV+AxTvtPR1FQrlqbhTJRwy+pw4KPJ7P4fq2R/YBqvXSNBC
amTt6l2XdXqnAk3A++cOEZ2lU9ubfgdeN2Ih8rgdn1LWeOSjCWfExmkoU61/Xe6x
AMeXKQSlHKSnX9voxuE2xINHeU6ZAKy1kGmrJtEiWnI8b8C4s8fTyDtXJ1Lasys0
iHO2Tz2jUhf4IJwb87Lk7Ize2MrI+oPzVDXlmkbjkB4tYyoiRTj8rk8pwBW/HVv0
02pjOLTa4kz1kQ3lsZ/3As4zfNi7mWEhadmEsAIfYkkCggEBANO39r/Yqj5kUyrm
ZXnVxyM2AHq58EJ4I4hbhZ/vRWbVTy4ZRfpXeo4zgNPTXXvCzyT/HyS53vUcjJF7
PfPdpXX2H7m/Fg+8O9S8m64mQHwwv5BSQOecAnzkdJG2q9T/Z+Sqg1w2uAbtQ9QE
kFFvA0ClhBfpSeTGK1wICq3QVLOh5SGf0fYhxR8wl284v4svTFRaTpMAV3Pcq2JS
N4xgHdH1S2hkOTt6RSnbklGg/PFMWxA3JMKVwiPy4aiZ8DhNtQb1ctFpPcJm9CRN
ejAI06IAyD/hVZZ2+oLp5snypHFjY5SDgdoKL7AMOyvHEdEkmAO32ot/oQefOLTt
GOzURVUCggEBALSx5iYi6HtT2SlUzeBKaeWBYDgiwf31LGGKwWMwoem5oX0GYmr5
NwQP20brQeohbKiZMwrxbF+G0G60Xi3mtaN6pnvYZAogTymWI4RJH5OO9CCnVYUK
nkD+GRzDqqt97UP/Joq5MX08bLiwsBvhPG/zqVQzikdQfFjOYNJV+wY92LWpELLb
Lso/Q0/WDyExjA8Z4lH36vTCddTn/91Y2Ytu/FGmCzjICaMrzz+0cLlesgvjZsSo
MY4dskQiEQN7G9I/Z8pAiVEKlBf52N4fYUPfs/oShMty/O5KPNG7L0nrUKlnfr9J
rStC2l/9FK8P7pgEbiD6obY11FlhMMF8udECggEBAIKhvOFtipD1jqDOpjOoR9sK
/lRR5bVVWQfamMDN1AwmjJbVHS8hhtYUM/4sh2p12P6RgoO8fODf1vEcWFh3xxNZ
E1pPCPaICD9i5U+NRvPz2vC900HcraLRrUFaRzwhqOOknYJSBrGzW+Cx3YSeaOCg
nKyI8B5gw4C0G0iL1dSsz2bR1O4GNOVfT3R6joZEXATFo/Kc2L0YAvApBNUYvY0k
bjJ/JfTO5060SsWftf4iw3jrhSn9RwTTYdq/kErGFWvDGJn2MiuhMe2onNfVzIGR
mdUxHwi1ulkspAn/fmY7f0hZpskDwcHyZmbKZuk+NU/FJ8IAcmvk9y7m25nSSc8=
-----END RSA PRIVATE KEY-----"""

EXPECTED_RESPONSE_FROM_DEVO = [{'eventdate': 1623069714735,
                                'technology': 'my', 'brand': 'app', 'phylum': 'cisco', 'family': 'amp',
                                'genus': 'cloudlogs', 'species': '',
                                'tables': [['my', 'synthesis', 'ciscodleval', 'amp', 'dfc'],
                                           ['my', 'synthesis', 'ciscodleval', 'eventlogs', 'example'], ['my', 'app'],
                                           ['my', 'synthesis', 'ciscodleval', 'ampevent', 'exprev1'],
                                           ['my', 'app', 'ciscodleval', 'cisco', 'amp'],
                                           ['my', 'synthesis', 'ciscodleval', 'jib'],
                                           ['my', 'synthesis', 'ciscodleval', 'ampevent', 'detection'],
                                           ['my', 'synthesis', 'ciscodleval', 'custom', 'table'],
                                           ['my', 'app', 'ciscodleval', 'cisco']], 'hostName': 'relay-01',
                                'hostIp': '172.25.1.47',
                                'message': '{"qt":26,"ip":"10.213.37.102","pip":"10.213.1.12","ti":13,"tv":5,"sbc":{'
                                           '"bin":165,"bout":183},"pr":52,"ets":1613439070,"ts":1613439073,'
                                           '"tsns":516833139,"uu":"7924dcfe-7d21-4dc6-8c24-694ee55f98b9","ai":1,'
                                           '"bg":"40041f5a-a8ad-4c29-9fda-d9b8ee966a6e","aptus":887,"ptus":905,'
                                           '"nfm":{"dir":1,"proto":6,"nt":1},"lip":{"ip":"192.168.43.199","p":53636},'
                                           '"rip":{"ip":"27.123.176.106","p":80},"liptr":{"ip":"192.168.43.199",'
                                           '"cidr":0,"dir":0,"proto":0},"riptr":{"ip":"27.123.176.106","cidr":0,'
                                           '"dir":0,"proto":0},"lipcr":{"ia":0,"ic":0,"id":1},"ripcr":{"ia":0,"ic":0,'
                                           '"id":1},"psha256":{'
                                           '"h":"DD191A5B23DF92E12A8852291F9FB5ED594B76A28A5A464418442584AFD1E048",'
                                           '"fa":-1964203938,"fs":53744,"ft":1,"hd":2},"rd":1,"ra":2,'
                                           '"tree":[{"tn":"FireAMP.IPBlacklist.MediumRisk","td":1,"tl":3},'
                                           '{"tn":"Infected.Bothost.LowRisk","td":1,"tl":3},'
                                           '{"tn":"Infected.Malware.MediumRisk","td":1,"tl":1},'
                                           '{"tn":"Infected.TalosResponse.MediumRisk","td":1,"tl":1},'
                                           '{"tn":"CnC.Host.MediumRisk","td":1,"tl":3},'
                                           '{"tn":"Infected.RET.Cryptomining.MediumRisk","td":1,"tl":3},'
                                           '{"tn":"Infected.Cryptomining.MediumRisk","td":1,"tl":1},'
                                           '{"tn":"CustomIPList","td":1,"tl":3}]}'},
                               {'eventdate': 1623069714735, 'technology': 'my', 'brand': 'app', 'phylum': 'cisco',
                                'family': 'amp', 'genus': 'cloudlogs', 'species': '',
                                'tables': [['my', 'synthesis', 'ciscodleval', 'amp', 'dfc'],
                                           ['my', 'synthesis', 'ciscodleval', 'eventlogs', 'example'], ['my', 'app'],
                                           ['my', 'synthesis', 'ciscodleval', 'ampevent', 'exprev1'],
                                           ['my', 'app', 'ciscodleval', 'cisco', 'amp'],
                                           ['my', 'synthesis', 'ciscodleval', 'jib'],
                                           ['my', 'synthesis', 'ciscodleval', 'ampevent', 'detection'],
                                           ['my', 'synthesis', 'ciscodleval', 'custom', 'table'],
                                           ['my', 'app', 'ciscodleval', 'cisco']], 'hostName': 'relay-01',
                                'hostIp': '172.25.1.47',
                                'message': '{"qt":26,"ip":"10.213.37.102","pip":"10.213.1.12","ti":15,"tv":5,"sbc":{'
                                           '"bin":165,"bout":183},"pr":52,"ets":1613439072,"ts":1613439073,'
                                           '"tsns":520537224,"uu":"7924dcfe-7d21-4dc6-8c24-694ee55f98b9","ai":1,'
                                           '"bg":"40041f5a-a8ad-4c29-9fda-d9b8ee966a6e","aptus":76,"ptus":99,'
                                           '"nfm":{"dir":1,"proto":6,"nt":1},"lip":{"ip":"192.168.43.199","p":53639},'
                                           '"rip":{"ip":"27.123.176.106","p":80},"liptr":{"ip":"192.168.43.199",'
                                           '"cidr":0,"dir":0,"proto":0},"riptr":{"ip":"27.123.176.106","cidr":0,'
                                           '"dir":0,"proto":0},"lipcr":{"ia":0,"ic":0,"id":1},"ripcr":{"ia":0,"ic":0,'
                                           '"id":1},"psha256":{'
                                           '"h":"DD191A5B23DF92E12A8852291F9FB5ED594B76A28A5A464418442584AFD1E048",'
                                           '"fa":-1964203936,"fs":53744,"ft":1,"hd":2},"rd":1,"ra":2,'
                                           '"tree":[{"tn":"FireAMP.IPBlacklist.MediumRisk","td":1,"tl":3},'
                                           '{"tn":"Infected.Bothost.LowRisk","td":1,"tl":3},'
                                           '{"tn":"Infected.Malware.MediumRisk","td":1,"tl":1},'
                                           '{"tn":"Infected.TalosResponse.MediumRisk","td":1,"tl":1},'
                                           '{"tn":"CnC.Host.MediumRisk","td":1,"tl":3},'
                                           '{"tn":"Infected.RET.Cryptomining.MediumRisk","td":1,"tl":3},'
                                           '{"tn":"Infected.Cryptomining.MediumRisk","td":1,"tl":1},'
                                           '{"tn":"CustomIPList","td":1,"tl":3}]}'}]


def base_payload():
    return {
        "data": {
            "sightings": {
                "count": 2,
                "docs": [
                    {
                        "confidence": "High",
                        "count": 1,
                        "data": {
                            "columns": [
                                {
                                    "name": "technology",
                                    "type": "string"
                                },
                                {
                                    "name": "brand",
                                    "type": "string"
                                },
                                {
                                    "name": "phylum",
                                    "type": "string"
                                },
                                {
                                    "name": "family",
                                    "type": "string"
                                },
                                {
                                    "name": "genus",
                                    "type": "string"
                                }
                            ],
                            "rows": [
                                [
                                    "my",
                                    "app",
                                    "cisco",
                                    "amp",
                                    "cloudlogs"
                                ]
                            ]
                        },
                        "description": "```\n{\"qt\":26,\"ip\":\"10.213.37.102\",\"pip\":\"10.213.1.12\",\"ti\":13,"
                                       "\"tv\":5,\"sbc\":{\"bin\":165,\"bout\":183},\"pr\":52,\"ets\":1613439070,"
                                       "\"ts\":1613439073,\"tsns\":516833139,"
                                       "\"uu\":\"7924dcfe-7d21-4dc6-8c24-694ee55f98b9\",\"ai\":1,"
                                       "\"bg\":\"40041f5a-a8ad-4c29-9fda-d9b8ee966a6e\",\"aptus\":887,\"ptus\":905,"
                                       "\"nfm\":{\"dir\":1,\"proto\":6,\"nt\":1},\"lip\":{\"ip\":\"192.168.43.199\","
                                       "\"p\":53636},\"rip\":{\"ip\":\"27.123.176.106\",\"p\":80},\"liptr\":{"
                                       "\"ip\":\"192.168.43.199\",\"cidr\":0,\"dir\":0,\"proto\":0},\"riptr\":{"
                                       "\"ip\":\"27.123.176.106\",\"cidr\":0,\"dir\":0,\"proto\":0},\"lipcr\":{\"ia\":0,"
                                       "\"ic\":0,\"id\":1},\"ripcr\":{\"ia\":0,\"ic\":0,\"id\":1},\"psha256\":{"
                                       "\"h\":\"DD191A5B23DF92E12A8852291F9FB5ED594B76A28A5A464418442584AFD1E048\","
                                       "\"fa\":-1964203938,\"fs\":53744,\"ft\":1,\"hd\":2},\"rd\":1,\"ra\":2,\"tree\":[{"
                                       "\"tn\":\"FireAMP.IPBlacklist.MediumRisk\",\"td\":1,\"tl\":3},"
                                       "{\"tn\":\"Infected.Bothost.LowRisk\",\"td\":1,\"tl\":3},"
                                       "{\"tn\":\"Infected.Malware.MediumRisk\",\"td\":1,\"tl\":1},"
                                       "{\"tn\":\"Infected.TalosResponse.MediumRisk\",\"td\":1,\"tl\":1},"
                                       "{\"tn\":\"CnC.Host.MediumRisk\",\"td\":1,\"tl\":3},"
                                       "{\"tn\":\"Infected.RET.Cryptomining.MediumRisk\",\"td\":1,\"tl\":3},"
                                       "{\"tn\":\"Infected.Cryptomining.MediumRisk\",\"td\":1,\"tl\":1},"
                                       "{\"tn\":\"CustomIPList\",\"td\":1,\"tl\":3}]}\n```",
                        "id": "transient:sighting-13cc8c2a-f233-5814-a897-d378ef1cda2c",
                        "internal": True,
                        "observables": [
                            {
                                "type": "ip",
                                "value": "27.123.176.106"
                            }
                        ],
                        "observed_time": {
                            "start_time": "2021-06-07T12:41:54.735+00:00"
                        },
                        "schema_version": "1.1.6",
                        "short_description": "Devo received a log message from relay-01 containing the observable",
                        "source": "Devo",
                        "title": "Log message received by Devo in last 30 days contains observable",
                        "type": "sighting"
                    },
                    {
                        "confidence": "High",
                        "count": 1,
                        "data": {
                            "columns": [
                                {
                                    "name": "technology",
                                    "type": "string"
                                },
                                {
                                    "name": "brand",
                                    "type": "string"
                                },
                                {
                                    "name": "phylum",
                                    "type": "string"
                                },
                                {
                                    "name": "family",
                                    "type": "string"
                                },
                                {
                                    "name": "genus",
                                    "type": "string"
                                }
                            ],
                            "rows": [
                                [
                                    "my",
                                    "app",
                                    "cisco",
                                    "amp",
                                    "cloudlogs"
                                ]
                            ]
                        },
                        "description": "```\n{\"qt\":26,\"ip\":\"10.213.37.102\",\"pip\":\"10.213.1.12\",\"ti\":15,"
                                       "\"tv\":5,\"sbc\":{\"bin\":165,\"bout\":183},\"pr\":52,\"ets\":1613439072,"
                                       "\"ts\":1613439073,\"tsns\":520537224,"
                                       "\"uu\":\"7924dcfe-7d21-4dc6-8c24-694ee55f98b9\",\"ai\":1,"
                                       "\"bg\":\"40041f5a-a8ad-4c29-9fda-d9b8ee966a6e\",\"aptus\":76,\"ptus\":99,"
                                       "\"nfm\":{\"dir\":1,\"proto\":6,\"nt\":1},\"lip\":{\"ip\":\"192.168.43.199\","
                                       "\"p\":53639},\"rip\":{\"ip\":\"27.123.176.106\",\"p\":80},\"liptr\":{"
                                       "\"ip\":\"192.168.43.199\",\"cidr\":0,\"dir\":0,\"proto\":0},\"riptr\":{"
                                       "\"ip\":\"27.123.176.106\",\"cidr\":0,\"dir\":0,\"proto\":0},\"lipcr\":{\"ia\":0,"
                                       "\"ic\":0,\"id\":1},\"ripcr\":{\"ia\":0,\"ic\":0,\"id\":1},\"psha256\":{"
                                       "\"h\":\"DD191A5B23DF92E12A8852291F9FB5ED594B76A28A5A464418442584AFD1E048\","
                                       "\"fa\":-1964203936,\"fs\":53744,\"ft\":1,\"hd\":2},\"rd\":1,\"ra\":2,\"tree\":[{"
                                       "\"tn\":\"FireAMP.IPBlacklist.MediumRisk\",\"td\":1,\"tl\":3},"
                                       "{\"tn\":\"Infected.Bothost.LowRisk\",\"td\":1,\"tl\":3},"
                                       "{\"tn\":\"Infected.Malware.MediumRisk\",\"td\":1,\"tl\":1},"
                                       "{\"tn\":\"Infected.TalosResponse.MediumRisk\",\"td\":1,\"tl\":1},"
                                       "{\"tn\":\"CnC.Host.MediumRisk\",\"td\":1,\"tl\":3},"
                                       "{\"tn\":\"Infected.RET.Cryptomining.MediumRisk\",\"td\":1,\"tl\":3},"
                                       "{\"tn\":\"Infected.Cryptomining.MediumRisk\",\"td\":1,\"tl\":1},"
                                       "{\"tn\":\"CustomIPList\",\"td\":1,\"tl\":3}]}\n```",
                        "id": "transient:sighting-52fabb09-16d7-5827-a81d-8b5084c3b611",
                        "internal": True,
                        "observables": [
                            {
                                "type": "ip",
                                "value": "27.123.176.106"
                            }
                        ],
                        "observed_time": {
                            "start_time": "2021-06-07T12:41:54.735+00:00"
                        },
                        "schema_version": "1.1.6",
                        "short_description": "Devo received a log message from relay-01 containing the observable",
                        "source": "Devo",
                        "title": "Log message received by Devo in last 30 days contains observable",
                        "type": "sighting"
                    }
                ]
            }
        }
    }
