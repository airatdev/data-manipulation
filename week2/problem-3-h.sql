SELECT result FROM (
  SELECT A.docid, B.docid, SUM(A.count * B.count) AS result
  FROM frequency AS A JOIN frequency AS B ON A.term = B.term
  WHERE A.docid = '10080_txt_crude'
  AND B.docid = '17035_txt_earn'
  GROUP BY A.docid, B.docid
) x;
