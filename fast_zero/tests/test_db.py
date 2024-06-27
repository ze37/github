from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session):
    user = User(
        username='zenetO',
        password='senha123',
        email='ze@ssauro.com',
    )
    session.add(user)
    session.commit()
    result = session.scalar(select(User).where(User.email == 'ze@ssauro.com'))
    assert result.username == 'zenetO'
