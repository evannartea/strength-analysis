CREATE TABLE staging.openpowerlifting_20260801 AS
SELECT
	"Name",
	"Sex",
	"Age",
	"BodyweightKg",
	"Country",
	"Date"::date AS "Date",
	"Best3SquatKg",
	"Best3BenchKg",
	"Best3DeadliftKg",
	"TotalKg",
	"Place"
FROM raw.openpowerlifting_20260801
WHERE "Age" >= 18
AND "Sex" <> 'Mx'
AND "Event"  = 'SBD'
AND "Equipment" = 'Raw'
AND "Place" NOT IN ('DQ', 'DD', 'NS')
ORDER BY "Date" DESC