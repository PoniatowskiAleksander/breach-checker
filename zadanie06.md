PS C:\studia\sem3\wirtualizzcje\lab\lab5\breach-checker> docker compose exec backend pytest -v
================================================= test session starts =================================================
platform linux -- Python 3.12.16, pytest-8.4.2, pluggy-1.7.0 -- /usr/local/bin/python3.12
cachedir: .pytest_cache
rootdir: /app
collected 7 items                                                                                                     

tests/test_check.py::test_leaked_hash_is_found PASSED                                                           [ 14%]
tests/test_check.py::test_unknown_hash_is_not_found PASSED                                                      [ 28%]
tests/test_check.py::test_missing_hash_field PASSED                                                             [ 42%] 
tests/test_check.py::test_plaintext_password_is_rejected PASSED                                                 [ 57%] 
tests/test_check.py::test_uppercase_hash_is_found PASSED                                                        [ 71%]
tests/test_check.py::test_short_hash_is_rejected PASSED                                                         [ 85%] 
tests/test_check.py::test_invalid_hex_is_rejected PASSED                                                        [100%]

================================================== 7 passed in 0.33s ==================================================
PS C:\studia\sem3\wirtualizzcje\lab\lab5\breach-checker> docker compose exec backend pytest
================================================= test session starts =================================================
platform linux -- Python 3.12.16, pytest-8.4.2, pluggy-1.7.0 -- /usr/local/bin/python3.12
cachedir: .pytest_cache
rootdir: /app
collected 7 items                                                                                                     

tests/test_check.py::test_leaked_hash_is_found PASSED                                                           [ 14%]
tests/test_check.py::test_unknown_hash_is_not_found PASSED                                                      [ 28%]
tests/test_check.py::test_missing_hash_field PASSED                                                             [ 42%] 
tests/test_check.py::test_plaintext_password_is_rejected PASSED                                                 [ 57%] 
tests/test_check.py::test_uppercase_hash_is_found FAILED                                                        [ 71%]
tests/test_check.py::test_short_hash_is_rejected PASSED                                                         [ 85%] 
tests/test_check.py::test_invalid_hex_is_rejected PASSED                                                        [100%] 

====================================================== FAILURES =======================================================
____________________________________________ test_uppercase_hash_is_found _____________________________________________

client = <FlaskClient <Flask 'app'>>

    def test_uppercase_hash_is_found(client):
        response = client.post("/check", json={"hash": LEAKED.upper()})
>       assert response.status_code == 200
E       assert 400 == 200
E        +  where 400 = <WrapperTestResponse streamed [400 BAD REQUEST]>.status_code

tests/test_check.py:27: AssertionError
=============================================== short test summary info ===============================================
FAILED tests/test_check.py::test_uppercase_hash_is_found - assert 400 == 200
============================================= 1 failed, 6 passed in 0.50s =============================================
PS C:\studia\sem3\wirtualizzcje\lab\lab5\breach-checker> 