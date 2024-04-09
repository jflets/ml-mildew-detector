mkdir -p ~/.streamlit/
cp .streamlit/config.toml ~/.streamlit/
echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
" >> ~/.streamlit/config.toml