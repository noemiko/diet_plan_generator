# diet_plan_generator

App to generate weekly diet plan based on AIP requirements.
Planner generate shop list for each day and for whole week.
It will also contains information how requirements are fulfilled.

Available scripts
```
docker-compose run --rm web python manage.py weekly_plan_generator
 docker-compose run --rm web python manage.py data_loader -f /usr/src/app/recipes/management/commands/cocktails.json
```

diet_plan_generator git:(poetry) ✗ docker-compose run --rm web poetry run pytest
