from housing.pipeline.pipeline import Pipeline
from housing.config.configuration import Configuartion
def main():
    try:
        pipeline = Pipeline(config=Configuartion())
        pipeline.run_pipeline()

        
    except Exception as e:
        print(e)



if __name__ == "__main__":
    main()