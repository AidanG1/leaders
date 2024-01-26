CREATE OR REPLACE FUNCTION leaderboard(leaderboard_category text)
RETURNS TABLE (
  leader_name text,
  image_url text,
  wikipedia_link text,
  total_wins bigint,
  total_losses bigint,
  win_percentage numeric
) AS
$$
DECLARE

BEGIN
  RETURN QUERY
  SELECT
    leaders.name as leader_name,
    leaders.image_url,
    leaders.wikipedia_link,
    COUNT(CASE WHEN votes.winner = leaders.id THEN 1 END) AS total_wins,
    COUNT(CASE WHEN votes.winner != leaders.id THEN 1 END) AS total_losses,
    COUNT(CASE WHEN votes.winner = leaders.id THEN 1 END)::numeric / COUNT(*)::numeric AS win_percentage
  FROM
    leader_categories
  JOIN
    leaders
  ON
    leaders.wikipedia_link = leader_categories.leader
  JOIN
    votes
  ON
    votes.winner = leaders.id or votes.loser = leaders.id
  WHERE
    votes.category = leaderboard_category
  GROUP BY
    leaders.id
  ORDER BY
    win_percentage DESC, total_wins DESC, total_losses ASC;

END;
$$
LANGUAGE plpgsql;

SELECT * FROM leaderboard('current');