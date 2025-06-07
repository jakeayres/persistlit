import streamlit as st


def _store_value(key):
    # Safely initialize both keys if missing
    if key not in st.session_state:
        st.session_state[key] = None
    if f"_{key}" not in st.session_state:
        st.session_state[f"_{key}"] = None
    st.session_state[key] = st.session_state["_"+key]


def _load_value(key):
    # Safely initialize both keys if missing
    if key not in st.session_state:
        st.session_state[key] = None
    if f"_{key}" not in st.session_state:
        st.session_state[f"_{key}"] = None
    st.session_state[f"_{key}"] = st.session_state[key]
    return st.session_state[f"_{key}"]


def _ensure_key_exist(key):
    if key not in st.session_state:
        st.session_state[key] = None
        
        
def _ensure_underscore_key_exist(key):
    if f"_{key}" not in st.session_state:
        st.session_state[f"_{key}"] = None


def get(key):
    return st.session_state[key]


def set(key, value):
    _ensure_key_exist(key)
    st.session_state[key] = value    
        
    

def text_input(key, **kwargs):
    _ensure_key_exist(key)
    _ensure_underscore_key_exist(key)
    if kwargs.get("default", None) is not None:
        set(key, kwargs['default'])
        kwargs.pop("default")
    st.text_input(
        label=kwargs.pop("label", key),
        value=_load_value(key),
        key=f"_{key}",
        on_change=_store_value, 
        args=[key],
        **kwargs,
    )
    return st.session_state[key]


def number_input(key, **kwargs):
    _ensure_key_exist(key)
    _ensure_underscore_key_exist(key)
    if kwargs.get("default", None) is not None:
        set(key, kwargs['default'])
        kwargs.pop("default")
    st.number_input(
        label=kwargs.pop("label", key),
        value=_load_value(key),
        key=f"_{key}",
        on_change=_store_value, 
        args=[key],
        **kwargs,
    )
    return st.session_state[key]


def pills(key, *args, **kwargs):
    _ensure_key_exist(key)
    _ensure_underscore_key_exist(key)
    if kwargs.get("default", None) is not None:
        set(key, kwargs['default'])
        kwargs.pop("default")
    st.pills(
        label=kwargs.pop("label", key),
        default=_load_value(key),
        key=f"_{key}",
        on_change=_store_value, 
        args=[key],
        *args, 
        **kwargs,
    )
    return st.session_state[key]



