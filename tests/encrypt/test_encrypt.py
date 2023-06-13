from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(6, 4)

    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("message", "invalidkey")

    assert encrypt_message("maca", 3) == "cam_a"

    assert encrypt_message("maca", 2) == "ac_am"

    assert encrypt_message("maca", 5) == "acam"
