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
