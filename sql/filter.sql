CREATE TABLE staging.openpowerlifting_20260801 AS
SELECT
	"Name",
	"Sex",
	"Age",
	"AgeClass"
	"BodyweightKg",
	"WeightClassKg",
	"Country",
	"Date"::date AS "Date",
	"Best3SquatKg" AS "SquatKg",
	"Best3BenchKg" AS "BenchKg",
	"Best3DeadliftKg" AS "DeadliftKg",
	"TotalKg",
	"Place"::int
FROM raw.openpowerlifting_20260801
WHERE "Age" >= 18
AND "Sex" <> 'Mx'
AND "Event"  = 'SBD'
AND "Equipment" = 'Raw'
AND "Place" NOT IN ('G', 'DQ', 'DD', 'NS')
ORDER BY "Date" DESC;