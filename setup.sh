mkdir -p ~/.streamlit/
echo "\
[general]\n\
email = \"dev@addicted.coffee\"\n\
" > ~/.streamlit/credentials.toml
echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
