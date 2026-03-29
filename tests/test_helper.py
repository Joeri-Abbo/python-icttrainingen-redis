from unittest.mock import patch, MagicMock
import redis
from classes import helper


def test_get_redis_connection_returns_redis_instance():
    conn = helper.get_redis_connection()
    assert isinstance(conn, redis.Redis)


def test_get_redis_connection_default_params():
    with patch("redis.Redis") as mock_redis:
        mock_redis.return_value = MagicMock()
        conn = helper.get_redis_connection()
        mock_redis.assert_called_once_with(host="localhost", port=6379, db=0)


def test_redis_set_and_get():
    mock_conn = MagicMock()
    mock_conn.get.return_value = b"10"

    with patch.object(helper, "get_redis_connection", return_value=mock_conn):
        conn = helper.get_redis_connection()
        conn.set("cabbage_qty", 10)
        result = conn.get("cabbage_qty")

    assert result == b"10"


def test_redis_sadd_and_smembers():
    mock_conn = MagicMock()
    mock_conn.sadd.return_value = 3
    mock_conn.smembers.return_value = {b"carrot", b"cabbage", b"capsicum"}

    with patch.object(helper, "get_redis_connection", return_value=mock_conn):
        conn = helper.get_redis_connection()
        added = conn.sadd("vegetables_instock", "carrot", "cabbage", "capsicum")
        members = conn.smembers("vegetables_instock")

    assert added == 3
    assert b"carrot" in members
    assert b"cabbage" in members
    assert b"capsicum" in members
