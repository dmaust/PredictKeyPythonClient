# PredictKey Python Client

Example Python Client for PredictKey.

Endpoint: http://api.predictkey.com/predict

Example POST:

    {
        "text":"Type your text here. It will use context of past text to predict the next word that is most ...",
        "apikey":"demo"
    }


Response:

    {
        "results": [
            {
                "prior": -3.77239405618921,
                "score": -0.626068288372828,
                "word": "likely"
            },
            {
                "prior": -5.2020142630638,
                "score": -0.707873701765409,
                "word": "definitely"
            },
            {
                "prior": -3.30694747736232,
                "score": -0.752443620568347,
                "word": "important"
            },
            {
                "prior": -3.36428114299092,
                "score": -0.766070099889562,
                "word": "people"
            },
            {
                "prior": -4.55066303362319,
                "score": -0.787643448685812,
                "word": "beautiful"
            },
            {
                "prior": -5.47755672727164,
                "score": -0.878634057428929,
                "word": "cases"
            },
            {
                "prior": -1.42226291977572,
                "score": -0.912725041185581,
                "word": "of"
            },
            {
                "prior": -4.24417850887813,
                "score": -0.943614258109723,
                "word": "part"
            },
            {
                "prior": -5.43806553884962,
                "score": -0.9575223361102,
                "word": "effective"
            },
            {
                "prior": -6.09051568318405,
                "score": -0.968367472987367,
                "word": "things"
            },
            {
                "prior": -5.34679189852768,
                "score": -0.989676240994535,
                "word": "difficult"
            },
            {
                "prior": -6.09051568318405,
                "score": -0.995963473763023,
                "word": "talented"
            },
            {
                "prior": -4.8327856164871,
                "score": -1.02361577276957,
                "word": "importantly"
            },
            {
                "prior": -5.07539520649558,
                "score": -1.02811750886854,
                "word": "interesting"
            },
            {
                "prior": -4.09095325214485,
                "score": -1.0393151092023,
                "word": "recent"
            },
            {
                "prior": -5.97409714697456,
                "score": -1.04097688358468,
                "word": "fun"
            },
            {
                "prior": -5.87773319269285,
                "score": -1.05191123340281,
                "word": "wonderful"
            },
            {
                "prior": -6.09546511865889,
                "score": -1.05631863951722,
                "word": "the"
            },
            {
                "prior": -4.92485512294686,
                "score": -1.06113763340474,
                "word": "powerful"
            },
            {
                "prior": -5.62162761340173,
                "score": -1.06239200462663,
                "word": "other"
            },
            {
                "prior": -4.24978022081204,
                "score": -1.06795522992351,
                "word": "popular"
            },
            {
                "prior": -5.3374013082734,
                "score": -1.07168960659677,
                "word": "often"
            },
            {
                "prior": -5.44584104369525,
                "score": -1.07675512987944,
                "word": "about"
            },
            {
                "prior": -6.04231795133081,
                "score": -1.08513765461029,
                "word": "serious"
            },
            {
                "prior": -4.84852322731499,
                "score": -1.09250741754083,
                "word": "amazing"
            },
            {
                "prior": -5.35865431809656,
                "score": -1.09939791472943,
                "word": "valuable"
            },
            {
                "prior": -6.0517742935967,
                "score": -1.11411045982956,
                "word": "welcome"
            },
            {
                "prior": -5.51586493395433,
                "score": -1.12644192542771,
                "word": "exciting"
            },
            {
                "prior": -5.20610996813512,
                "score": -1.14223564173031,
                "word": "in"
            },
            {
                "prior": -5.43548696619719,
                "score": -1.17179143268129,
                "word": "expensive"
            },
            {
                "prior": -5.73286987912052,
                "score": -1.1768243161701,
                "word": "memorable"
            },
            {
                "prior": -5.78980131544908,
                "score": -1.18200879966437,
                "word": "is"
            },
            {
                "prior": -5.63723586970169,
                "score": -1.18919165578284,
                "word": "days"
            },
            {
                "prior": -6.10043906171087,
                "score": -1.1970811244343,
                "word": "obvious"
            },
            {
                "prior": -5.9963267879508,
                "score": -1.21009305203731,
                "word": "to"
            },
            {
                "prior": -5.00067759416436,
                "score": -1.21574059643622,
                "word": "recently"
            },
            {
                "prior": -5.38770615974164,
                "score": -1.24283822848644,
                "word": "successful"
            },
            {
                "prior": -5.5732467920889,
                "score": -1.2486324240334,
                "word": "certainly"
            },
            {
                "prior": -6.08068937504567,
                "score": -1.25325680526316,
                "word": "vulnerable"
            },
            {
                "prior": -4.96125195563373,
                "score": -1.32468159391563,
                "word": "common"
            },
            {
                "prior": -5.9829300904229,
                "score": -1.33110699001122,
                "word": "prominent"
            },
            {
                "prior": -5.78614716137174,
                "score": -1.41045305825432,
                "word": "americans"
            },
            {
                "prior": -5.72941637013662,
                "score": -1.41868236105519,
                "word": "notably"
            },
            {
                "prior": -4.82008826772819,
                "score": -1.42547760939823,
                "word": "famous"
            },
            {
                "prior": -6.0470349974467,
                "score": -1.4418867321629,
                "word": "i"
            },
            {
                "prior": -5.64354753505311,
                "score": -1.45479494942735,
                "word": "dangerous"
            },
            {
                "prior": -5.380364427121,
                "score": -1.49139663225196,
                "word": "are"
            },
            {
                "prior": -5.87374588437962,
                "score": -1.49358958379774,
                "word": "influential"
            },
            {
                "prior": -6.01905927699213,
                "score": -1.49371228426183,
                "word": "basic"
            },
            {
                "prior": -5.63723586970169,
                "score": -1.54821040692277,
                "word": "significant"
            }
        ]
    }
