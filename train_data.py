# training data
TRAIN_DATA = [
    (
        "Date Notice Posted: 2018/10/19 | Company: Goodman Manufacturing Company L.P. | County: Lincoln | Affected Workers: 81 | Closure/Layoff Date: December 21, 2018",
        {
            "entities": [
                (20, 30, "DATE_NOTICE_POSTED"),
                (42, 76, "COMPANY"),
                (87, 94, "COUNTY"),
                (115, 117, "AFFECTED_WORKERS"),
                (141, 158, "CLOSURE_LAYOFF_DATE")
            ]
        }
    ),
    (
        "Date Notice Posted: 2018/10/11 | Company: GSK Consumer Health - Global manufacturing & Supply | County: Shelby | Affected Workers: 99 | Closure/Layoff Date: December 10, 2018",
        {
            "entities": [
                (20, 30, "DATE_NOTICE_POSTED"),
                (42, 93, "COMPANY"),
                (104, 110, "COUNTY"),
                (131, 133, "AFFECTED_WORKERS"),
                (157, 174, "CLOSURE_LAYOFF_DATE")
            ]
        }
    ),
    (
        "Date Notice Posted: 2018/9/28 | Company: Youth Villages | County: Perry | Affected Workers: 87 | Closure/Layoff Date: November 25, 2018 | Notice/Type: #20180030",
        {
            "entities": [
                (20, 29, "DATE_NOTICE_POSTED"),
                (41, 55, "COMPANY"),
                (66, 71, "COUNTY"),
                (92, 94, "AFFECTED_WORKERS"),
                (118, 135, "CLOSURE_LAYOFF_DATE")
            ]
        }
    ),
    (
        "Date Notice Posted: 2023/3/2 | Company: National Seating & Mobility, Inc. | County: Hamilton | Affected Workers: 108 | Closure/Layoff Date: March 23, 2023 – July 28, 2023 | Notice/Type: #202300012",
        {
            "entities": [
                (20, 28, "DATE_NOTICE_POSTED"),
                (40, 73, "COMPANY"),
                (84, 92, "COUNTY"),
                (113, 116, "AFFECTED_WORKERS"),
                (140, 154, "CLOSURE_LAYOFF_DATE")
            ]
        }
    ),
    (
        "Date Notice Posted: 2023/2/27 | Company: American Car Center | County: Shelby | Affected Workers: 288 | Closure/Layoff Date: February 24, 2023 | Notice/Type: #02300011",
        {
            "entities": [
                (20, 29, "DATE_NOTICE_POSTED"),
                (41, 60, "COMPANY"),
                (71, 77, "COUNTY"),
                (98, 101, "AFFECTED_WORKERS"),
                (125, 142, "CLOSURE_LAYOFF_DATE")
            ]
        }
    ),
    (
        "Date Notice Posted: 2023/2/22 | Company: CEVA Logistics | County: Wilson | Affected Workers: 142 | Closure/Layoff Date: April 22, 2023 | Notice/Type: #202300010",
        {
            "entities": [
                (20, 29, "DATE_NOTICE_POSTED"),
                (41, 55, "COMPANY"),
                (66, 72, "COUNTY"),
                (93, 96, "AFFECTED_WORKERS"),
                (120, 134, "CLOSURE_LAYOFF_DATE")
            ]
        }
    ),
    (
        "Date Notice Posted: 2023/2/10 | Company: Befesa Zinc US Inc. | County: Roane | Affected Workers: 50 | Closure/Layoff Date: April 8, 2023 | Notice/Type: #202300009",
        {
            "entities": [
                (20, 29, "DATE_NOTICE_POSTED"),
                (41, 60, "COMPANY"),
                (71, 76, "COUNTY"),
                (97, 99, "AFFECTED_WORKERS"),
                (123, 136, "CLOSURE_LAYOFF_DATE")
            ]
        }
    ),
    (
        "Date Notice Posted: 2023/2/9 | Company: American Snuff Company, LLC | County: Shelby | Affected Workers: 132 | Closure/Layoff Date: December 1, 2023 | Notice/Type: #202300008",
        {
            "entities": [
                (20, 28, "DATE_NOTICE_POSTED"),
                (40, 67, "COMPANY"),
                (78, 84, "COUNTY"),
                (105, 108, "AFFECTED_WORKERS"),
                (132, 148, "CLOSURE_LAYOFF_DATE")
            ]
        }
    ),
    (
        "Date Notice Posted: 2023/2/8 | Company: ThyssenKrupp | County: Hamilton | Affected Workers: 156 | Closure/Layoff Date: May 6, 2023 – May 20, 2023 | Notice/Type: #202300007",
        {
            "entities": [
                (20, 28, "DATE_NOTICE_POSTED"),
                (40, 52, "COMPANY"),
                (63, 71, "COUNTY"),
                (92, 95, "AFFECTED_WORKERS"),
                (119, 145, "CLOSURE_LAYOFF_DATE")
            ]
        }
    ),
    (
        "Date Notice Posted: 2023/2/8 | Company: National Pen | County: Bedford | Affected Workers: 67 | Closure/Layoff Date: March 30, 2023 – May 31, 2023 | Notice/Type: #202300006",
        {
            "entities": [
                (20, 28, "DATE_NOTICE_POSTED"),
                (40, 52, "COMPANY"),
                (63, 70, "COUNTY"),
                (91, 93, "AFFECTED_WORKERS"),
                (117, 146, "CLOSURE_LAYOFF_DATE")
            ]
        }
    ),
    (
        "Date Notice Posted: 2017/10/26 | Company: Luxottica Retail North America Inc. | County: Shelby | Affected Workers: 208 | Closure/Layoff Date: December 31, 2017 | Notice/Type: WARN # 20170048",
        {
            "entities": [
                (20, 30, "DATE_NOTICE_POSTED"),
                (42, 77, "COMPANY"),
                (88, 94, "COUNTY"),
                (115, 118, "AFFECTED_WORKERS"),
                (142, 159, "CLOSURE_LAYOFF_DATE")
            ]
        }
    ),
    (
        "Date Notice Posted: 2019/11/12 | Company: Mitsubishi Electric Power Products, Inc. | County: Shelby | Affected Workers: 160 | Closure/Layoff Date: January 3, 2020 through January 31, 2020 | Notice/Type: #201900060",
        {
            "entities": [
                (20, 30, "DATE_NOTICE_POSTED"),
                (42, 82, "COMPANY"),
                (93, 99, "COUNTY"),
                (120, 123, "AFFECTED_WORKERS"),
                (147, 187, "CLOSURE_LAYOFF_DATE")
            ]
        }
    ),
    (
        "Date Notice Posted: 2019/11/1 | Company: Leidos | County: Shelby | Affected Workers: 107 | Closure/Layoff Date: December 31, 2019 | Notice/Type: #201900059",
        {
            "entities": [
                (20, 29, "DATE_NOTICE_POSTED"),
                (41, 47, "COMPANY"),
                (58, 64, "COUNTY"),
                (85, 88, "AFFECTED_WORKERS"),
                (112, 129, "LAYOFF_CLOSURE_DATE")
            ]
        }
    ),
    (
        "Date Notice Posted: 2019/10/7 | Company: Regal Beloit America Inc. | County: Unicoi | Affected Workers: 125 | Closure/Layoff Date: Will begin on November 30, 2019 and will continue to December 31, 2020 | Notice/Type: #201900045",
        {
            "entities": [
                (20, 29, "DATE_NOTICE_POSTED"),
                (41, 66, "COMPANY"),
                (77, 83, "COUNTY"),
                (104, 107, "AFFECTED_WORKERS"),
                (145, 162, "LAYOFF_CLOSURE_DATE")
            ]
        }
    ),
    # === WA TRAINING DATA ===#
    (
        "Company: Q2 Solutions Location: Seattle Layoff Start Date: 6/15/2023 # of Workers: 43 Closure Layoff: Closure Type of Layoff: Permanent Received Date: 4/3/2023 State: WA",
        {
    
        }
    ),
    (
        "Company: Microsoft Location: Redmond and Bellevue Layoff Start Date: 5/26/2023 # of Workers: 559 Closure Layoff: Layoff Type of Layoff: Permanent Received Date: 3/27/2023 State: WA",
        {
    
        }
    ),
    (
        "Company: Aspiration Partners, Inc Location: King and Snohomish Counties Layoff Start Date: 5/26/2023 # of Workers: 3 Closure Layoff: Layoff Type of Layoff: Permanent Received Date: 3/24/2023 State: WA",
        {
    
        }
    ),
    (
        "Company: Walmart Location: Everett Layoff Start Date: 6/30/2023 # of Workers: 198 Closure Layoff: Closure Type of Layoff: Permanent Received Date: 3/23/2023 State: WA",
        {
    
        }
    ),
    (
        "Company: Blue Nile, Inc. Location: Seattle Layoff Start Date: 7/14/2023 # of Workers: 119 Closure Layoff: Closure Type of Layoff: Permanent Received Date: 3/23/2023 State: WA",
        {
    
        }
    ),
    (
        "Company: Ace Hardware Corporation Location: Spokane Layoff Start Date: 5/17/2023 # of Workers: 86 Closure Layoff: Layoff Type of Layoff: Permanent Received Date: 3/17/2023 State: WA",
        {
    
        }
    ),
    (
        "Company: Astound Broadband Location: Bothell Layoff Start Date: 5/19/2023 # of Workers: 90 Closure Layoff: Layoff Type of Layoff: Permanent Received Date: 3/17/2023 State: WA",
        {
    
        }
    ),
    (
        "Company: Compass Group USA, Inc. Location: Redmond Layoff Start Date: 3/24/2023 # of Workers: 68 Closure Layoff: Layoff Type of Layoff: Permanent Received Date: 3/8/2023 State: WA",
        {
    
        }
    ),
    (
        "Company: Ingersoll Rand Location: Kent Layoff Start Date: 5/8/2023 # of Workers: 69 Closure Layoff: Closure Type of Layoff: Permanent Received Date: 3/7/2023 State: WA",
        {
    
        }
    ),
    (
        "Company: Microsoft Location: Redmond, Bellevue, Issaquah Layoff Start Date: 5/5/2023 # of Workers: 689 Closure Layoff: Layoff Type of Layoff: Permanent Received Date: 3/6/2023 State: WA",
        {
    
        }
    ),
    (
        "Company: Novo Nordisk Research Center Seattle, Inc Location: Seattle Layoff Start Date: 5/1/2023 # of Workers: 86 Closure Layoff: Layoff Type of Layoff: Permanent Received Date: 3/1/2023 State: WA",
        {
    
        }
    ),
    (
        "Company: FleetLogix, Inc Location: SeaTac, Tukwila Layoff Start Date: 4/28/2023 # of Workers: 120 Closure Layoff: Closure Type of Layoff: Permanent Received Date: 2/28/2023 State: WA",
        {
    
        }
    ),
    (
        "Company: Rume Medical Group Location: Seattle, Lynden Layoff Start Date: 2/26/2023 # of Workers: 2 Closure Layoff: Layoff Type of Layoff: Permanent Received Date: 2/24/2023 State: WA",
        {
    
        }
    ),
    (
        "Company: American Medical Response, Pierce County Location: Fife Layoff Start Date: 4/19/2023 # of Workers: 43 Closure Layoff: Closure Type of Layoff: Permanent Received Date: 2/17/2023 State: WA",
        {
    
        }
    ),
    (
        "Company: Critical Ideas, Inc. dba Chipper Cash Location: Vancouver, Spokane Layoff Start Date: 2/17/2023 # of Workers: 2 Closure Layoff: Layoff Type of Layoff: Permanent Received Date: 2/16/2023 State: WA",
        {
    
        }
    ),
    (
        "Company: Staples Location: Auburn Layoff Start Date: 11/17/2014 # of Workers: 50 Closure Layoff: Layoff Type of Layoff: Permanent Received Date: 9/17/2014 State: WA",
        {
            
        }
    ),
    (
        "Company: Microsoft Location: Redmond Layoff Start Date: 11/17/2014 # of Workers: 747 Closure Layoff: Layoff Type of Layoff: Permanent Received Date: 9/18/2014 State: WA",
        {
    
        }
    ),
    (
        "Company: Nordstrom Location: Vancouver Layoff Start Date: 1/10/2015 # of Workers: 142 Closure Layoff: Closure Type of Layoff: Permanent Received Date: 10/31/2014 State: WA",
        {
    
        }
    ),
    (
        "Company: Avamere Georgian House of Lakewood Location: Lakewood WA Layoff Start Date: 1/16/2015 # of Workers: 69 Closure Layoff: Closure Type of Layoff: Permanent Received Date: 11/12/2014 State: WA",
        {
    
        }
    ),
    (
        "Company: Bradken Foundry Location: Chehalis Layoff Start Date: 3/16/2015 # of Workers: 89 Closure Layoff: Closure Type of Layoff: Permanent Received Date: 1/15/2015 State: WA",
        {
    
        }
    ),
    (
        "Company: Great American Casino Location: Kent Layoff Start Date: 3/15/2015 # of Workers: 93 Closure Layoff: Closure Type of Layoff: Permanent Received Date: 1/26/2015 State: WA",
        {
    
        }
    ),
    (
        "Company: Lionbridge Location: Vancouver Layoff Start Date: 6/10/2018 # of Workers: 119 Closure Layoff: Layoff Type of Layoff: Permanent Received Date: 4/6/2018 State: WA",
        {
    
        }
    ),
    (
        "Company: Skagit Bank Location: Burlington Layoff Start Date: 3/1/2019 # of Workers: 60 Closure Layoff: Closure Type of Layoff: Permanent Received Date: 1/22/2019 State: WA",
        {
    
        }
    ),
    # === CA TRAINING DATA === #
    (
        "Notice Date: 06/02/2022, Effective Date: 08/08/2022, Company: Silgan Containers, Affected Workers: 80, Stanislaus County",
        {
    
        }
    ),
    (
        "Notice Date: 06/21/2022, Effective Date: 08/22/2022, Company: Yanka Industries, Inc. dba MasterClass, Affected Workers: 95, San Francisco County",
        {
    
        }
    ),
    (
        "Notice Date: 06/15/2022, Effective Date: 08/15/2022, Company: Azusa Pacific University, Affected Workers: 29, Los Angeles County",
        {
            
        }
    ),
    (
        "Notice Date: 05/24/2022, Effective Date: 07/25/2022, Company: Illume Ag HR, Inc., Affected Workers: 186, Riverside County",
        {
    
        }
    ),
    (
        "Notice Date: 06/02/2022, Effective Date: 07/04/2022, Company: Wells Fargo, Affected Workers: 1, San Bernardino County",
        {
    
        }
    ),
    (
        "Notice Date: 05/02/2022, Effective Date: 06/17/2022, Company: Blend Labs, Inc., Affected Workers: 89, Orange County",
        {
    
        }
    ),
    (
        "Notice Date: 04/29/2022, Effective Date: 06/30/2022, Company: Morrison Healthcare at Kaiser Permanente-Walnut Creek, Affected Workers: 5, Los Angeles County",
        {
    
        }
    ),
    (
        "Notice Date: 04/29/2022, Effective Date: 05/06/2022, Company: Whole Foods Market, Affected Workers: 117, Los Angeles County",
        {
    
        }
    ),
    (
        "Notice Date: 04/25/2022, Effective Date: 08/31/2022, Company: Marymount California University, Affected Workers: 131, Los Angeles County",
        {
    
        }
    ),
    (
        "Notice Date: 12/17/2021, Effective Date: 02/15/2022, Company: Med-Legal, LLC, Affected Workers: 113, Los Angeles County",
        {
    
        }
    ),
    (
        "Notice Date: 11/16/2021, Effective Date: 01/28/2022, Company: TE Connectivity, Affected Workers: 31, Santa Clara County",
        {
    
        }
    ),
    (
        "Notice Date: 10/05/2021, Effective Date: 12/03/2021, Company: Safran Cabin Inc., Affected Workers: 93, San Bernardino County",
        {
    
        }
    ),
    (
        "Notice Date: 08/27/2021, Effective Date: 10/31/2021, Company: State Farm Mutual Automobile Insurance Company, Affected Workers: 230, Kern County",
        {
    
        }
    ),
    (
        "Notice Date: 08/16/2021, Effective Date: 09/25/2021, Company: Chick-fil-A, Inc., Affected Workers: 110, San Bernardino County",
        {
    
        }
    ),
    (
        "Notice Date: 05/17/2022, Effective Date: 04/28/2022, Company: Netflix, Inc., Affected Workers: 106, County: Los Angeles County",
        {
    
        }
    ),
    (
        "Notice Date: 03/04/2022, Effective Date: 05/06/2022, Company: Nestle USA, Inc, Affected Workers: 104, County: Monterey County",
        {
    
        }
    ),
    (
        "Notice Date: 02/15/2022, Effective Date: 05/20/2022, Company: Walmart, Affected Workers: 105, County: Orange County",
        {
    
        }
    ),
    (
        "Notice Date: 01/27/2022, Effective Date: 04/01/2022, Company: Herbalife International of America, Inc., Affected Workers: 3, County: Los Angeles County",
        {
    
        }
    ),
    (
        "Notice Date: 01/27/2022, Effective Date: 03/31/2022, Company: Davidson Hotel Company LLC dba Pivot Hotels and resorts at Bei Hotel San Francisco, Affected Workers: 110, County: San Francisco County",
        {
    
        }
    ),
    (
        "Notice Date: 01/27/2022, Effective Date: 03/28/2022, Company: Beachbody LLC, Affected Workers: 70, County: Los Angeles County",
        {
    
        }
    ),
    (
        "Notice Date: 12/16/2021, Effective Date: 03/02/2022, Company: Wyndham Hotels & Resorts dba La Quinta Thousand Oaks-Newbury Park with L.Q. Management LLC, Affected Workers: 19, County: Ventura County",
        {
    
        }
    )
]