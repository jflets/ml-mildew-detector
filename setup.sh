mkdir -p ~/.streamlit/
echo "\
[server]
headless = true
port = $PORT
enableCORS = false

[theme]
base = 'dark'
primaryColor = '#48C626'
backgroundColor = '#42692E'
secondaryBackgroundColor = '#83937B'
textColor = '#ffffff'
font = 'Gill Sans'
" > ~/.streamlit/config.toml
