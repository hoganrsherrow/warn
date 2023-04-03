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
                (145, 162, "LAYOFF_CLOSURE_DATE"),
                (184, 201, "LAYOFF_CLOSURE_DATE")
            ]
        }
    )
]