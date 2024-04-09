mkdir -p ~/.streamlit/
echo "\
[server]
headless = true
port = $PORT
enableCORS = false
" > ~/.streamlit/config.toml

cp .streamlit/config.toml ~/.streamlit/config.toml
