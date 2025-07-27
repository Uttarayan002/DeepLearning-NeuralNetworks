from configs import Config
from data_loader import DataLoader
from model_builder import ANNModel
from trainer import ModelTrainer
from evaluator import Evaluator

def main():
    config = Config()
    loader = DataLoader("data.csv")
    X_train, X_test, y_train, y_test = loader.load_and_process()

    builder = ANNModel(config)
    model = builder.build_model()

    trainer = ModelTrainer(model, config)
    trainer.train(X_train, y_train, X_test, y_test)

    evaluator = Evaluator(model)
    evaluator.evaluate(X_test, y_test)

if __name__ == "__main__":
    main()
