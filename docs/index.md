# Persistlit

More convenient streamlit widgets that persist between pages.

## Objective

Perhaps you require a widget that persists between pages. This might be a configuration options or global variable that you would like to be able to access and adjust from multiple places within your app. It would be nice if something like this worked:

```python title="/pages/page1.py"
x = st.number_input("A number used across multiple pages", key='x')
st.write(x)
st.write(st.session_state.get('x', None))

do_something_with_x(x)
```

```python title="/pages/page2.py"
x = st.number_input("A number used across multiple pages", key='x')
st.write(x)
st.write(st.session_state.get('x', None))

do_something_different_with_x(x)
```

With each page load, both `x` and `session_state["x"]` are overwritten by the instantiated widget. Neither the displayed widget value nor `x` nor `session_state["x"]` are persisted as `x` is set to an empty string each time the widget is rendered.

## Native Streamlit Solution

This can be solved with some fiddling with the session_state and default arguments:


## Persistlit Solution