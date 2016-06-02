SELECT count(*) FROM (
  SELECT DISTINCT docid FROM frequency WHERE term='world' INTERSECT
  SELECT DISTINCT docid FROM frequency WHERE term='transactions'
) x;
