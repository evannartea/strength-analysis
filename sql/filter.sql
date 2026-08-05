CREATE TABLE staging.openpowerlifting_20260801 AS
SELECT
	op."Name",
	op."Sex",
	op."Age",
	op."BodyweightKg",
	op."Country",
	op."Date"::date AS "Date",
	op."Best3SquatKg",
	op."Best3BenchKg",
	op."Best3DeadliftKg",
	op."TotalKg",
	op."Place"
FROM raw.openpowerlifting_20260801 op
WHERE op."Age" >= 18
AND op."Sex" <> 'Mx'
AND op."Event"  = 'SBD'
AND op."Equipment" = 'Raw'
AND op."Place" NOT IN ('DQ', 'DD', 'NS')
ORDER BY op."Date" DESC