-- SQL script that ranks country origins of bands, ordered by the number of (non-unique) fans
-- Requirements:
-- Import this table dump: metal_bands.sql.zip
-- Column names must be: origin and nb_fans
-- Your script can be executed on any database
SELECT origin, COUNT(*) AS nb_fans
FROM (
    SELECT DISTINCT band, fan
    FROM metal_bands
) AS distinct_fans
JOIN metal_bands ON distinct_fans.band = metal_bands.band AND distinct_fans.fan = metal_bands.fan
GROUP BY origin
ORDER BY nb_fans DESC;

