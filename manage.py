import os
from flask.cli import FlaskGroup
from app import create_app

app = create_app()
cli = FlaskGroup(app)

@cli.command("run")
def run():
    """运行开发服务器"""
    app.run(host='0.0.0.0', port=5000, debug=True)

@cli.command("init_db")
def init_db():
    """初始化数据库"""
    # 这里可以添加数据库初始化的代码
    print("数据库已初始化")

@cli.command("test")
def test():
    """运行单元测试"""
    import pytest
    pytest.main(["-v", "tests"])

if __name__ == '__main__':
    cli()
