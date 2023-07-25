# XYZ Marketing Data Pipeline

This is the result of automating a data pipeline for the XYZ marketing department. It
was developed in the notebook `pipeline.ipynb` which contains an explanation of each of
the decisions that went into it. For production purposes it has been refactored into
`pipeline.py`, which can be run via Docker by running the following commands:

```bash
docker build -t pipeline .
docker run -v "$(pwd)/exports:/app/exports" pipeline
```

All outputs are saved to the `exports` folder. If the code is run on the same file on
different days new identical files will be created with on the date it is run again
because the original data itself does not contain the date it was produced.

## Further work

1. We are currently trusting that the data will always be delivered the same. If we want
   to be more robust we could add validation checks to ensure it is in the format we
   expect.
2. We could add tests to ensure that future refactoring does not accidentally change the
   output.
3. We could add type hints to our code. It could be stored in a repository and run via
   CI/CD along with linting and tests. Ideally, it could be set to run on a regular
   schedule so that differences between runs are more meaningful.
4. We could add a dedicated env file so that changing the filename does not require
   editing Python code.
5. We could separate our pipeline in to multiple functions or methods. We don't want to
   do this too soon as to avoid overengineering before we have more complex
   requirements.
6. We could read from previous exports to see comparisons as time changes. What exactly
   would be useful would be best decided together with the marketing department.
7. We could add a frontend so that the marketing team could use their browser to upload
   the data and download the results.
