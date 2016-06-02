  SELECT COUNT(*) FROM(
    SELECT docid, COUNT(*) FROM frequency GROUP BY docid HAVING COUNT(*) > 300
  ) x;
