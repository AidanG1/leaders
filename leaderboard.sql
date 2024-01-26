CREATE OR REPLACE FUNCTION leaderboard()
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
    leaders
  JOIN
    votes
  ON
    votes.winner = leaders.id or votes.loser = leaders.id
  GROUP BY
    leaders.id
  ORDER BY
    win_percentage DESC, total_wins DESC, total_losses ASC;

END;
$$
LANGUAGE plpgsql;

grant execute on function leaderboard() to anon;

SELECT * FROM leaderboard();