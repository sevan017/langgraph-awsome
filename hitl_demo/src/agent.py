"""
@Author: wcy
@File: agent.py
@Date: 2026/8/6 8:07
@Desc: 
"""
from typing import TypedDict, Literal

from langgraph.constants import START, END
from langgraph.graph import StateGraph
from langgraph.types import interrupt


# 定义状态
class OverAllState(TypedDict):
    username: str  # 姓名
    age: int  # 年龄
    gender: Literal["male", "female"]  # 性别


def get_info_node(state: OverAllState) -> OverAllState:
    username = interrupt("请输入你的用户名：")
    age = interrupt("请输入您的年龄：")
    gender = interrupt("请输入你的性别: (male/female)")
    return {
        "username": username,
        "age": age,
        "gender": gender
    }


builder = StateGraph(state_schema=OverAllState)
builder.add_node("get_info_node", get_info_node)
builder.add_edge(START, "get_info_node")
builder.add_edge("get_info_node", END)

graph = builder.compile()
