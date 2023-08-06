TITLE = "FieldA,FieldB,Number,Value\n"
CSV_DATA = (f"{TITLE}"
            "DataA1,DataB1,42,Value1\n"
            "DataA2,DataB2,15,Value2\n"
            "DataA3,DataB3,78,Value3\n"
            "DataA4,DataB4,32,Value4\n"
            "DataA5,DataB5,60,Value5\n"
            "DataA6,DataB6,91,Value6\n"
            "DataA7,DataB7,24,Value7\n")
CSV_DATA_LINE_COUNT = CSV_DATA.count("\n")
CHUNKS = [
    ["FieldA,FieldB,Number,Value\n"
     "DataA1,DataB1,42,Value1\n"
     "DataA2,DataB2,15,Value2\n"],
    ["FieldA,FieldB,Number,Value\n"
     "DataA3,DataB3,78,Value3\n"
     "DataA4,DataB4,32,Value4\n"]
]
