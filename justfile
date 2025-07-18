setup:
  poetry sync

run *args:
  poetry run main.py {{ args }}

test:
  poetry minitest.py