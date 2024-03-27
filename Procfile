if [ "$HEROKU_ENV" == "production" ]; then
  pip install -r requirements.txt
else
  pip install -r dev_requirements.txt
fi

web: sh setup.sh && streamlit run app.py