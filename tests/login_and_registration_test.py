"""
Test for logging in and registration
"""

# def test_index_page_not_logged_in(client):
#     res = client.get('./dashboard')
#     assert res.status_code == 401

def test_profile_page_logged_in(client):
    with client:
        client.post('/login', data=dict(email='test@njit.edu', password='testtest'))
        res = client.get('/profile')
        assert res.status_code == 200

def test_user_registration(client):
    with client:
        res = client.post('/register', data=dict(email='register@njit.edu', password='testtest', confirm='testtest'), follow_redirects=True)
        assert res.status_code == 200



