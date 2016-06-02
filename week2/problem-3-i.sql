SELECT MAX(result) FROM (
  SELECT SUM(A.count) AS result
  FROM frequency AS A JOIN frequency AS B ON A.term = B.term
  WHERE a.term IN ('washington', 'taxes', 'treasury')
  AND b.term IN ('washington', 'taxes', 'treasury')
  GROUP BY A.docid, B.docid
);
