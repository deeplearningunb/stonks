# Stonks
Using deep learning to predict stock open and close prices.

## About
First of all we need to understand how the stocks market works.

### What is a stock?

<p align='justify'>A stock represents a fraction of the value of companies, so we can say that a stock is a small piece of a company. These stocks are traded in the stock exchange.

<p align='justify'>Nowadays, stocks are a type of investment that people are looking for, due to the great results they can present. However, the volatile of the stock market makes stock prices vary constantly. It brings several risks to investors.

<p align='justify'>On the other hand, this high frequency that stock prices changes is a feature enjoyed by those who invest in the stock market. These investors buy the stocks for a low price and sell for a higher price.

### How is our project related to this situation?

<p align='justify'>The Stonks project goal is to facilitate investor analysis of when is the right time to buy and sell stocks, since this neural network will be able to present predictions about the stocks opening and closing price.

<p align='justify'>In this way, Stonks will significantly help you achieve good results taking advantage of the  the market offers.

<p align="center">
  <img src="https://github.com/deeplearningunb/stonks/blob/master/img/mario.gif">
</p>

### How are we gonna make it works? 

<p align='justify'>In our project we use a Recurrent Neural Network - RNN and Long Term Short Memory - LSTM . But, do you know what a RNN is?

<p align='justify'>A Recurrent Neural Network is a class of artificial neural networks in which the connections of nodes forms directed graphs along a temporal line. But what is a neural network?

<p align='justify'>Artificial neural networks (ANN) are a set of algorithms modeled after the human brain. Those algorithms are designed to recognize patterns in various forms of data thats is converted to numerical form, and interpreted by a kind of machine perception, labeling or clustering raw input. Neural networks help cluster and classify data through different methods and architectures that try to achieve different goals. ANNs can use a variety of algorithms to compose their architecture as well as to process the data that comes through input.

<p align='justify'>Unlike other neural networks that use the feedfoward system RNNs can use memory to proccess sequential inputs through the architecture of Long term short memory (LSTM). LSTM is used in RNNs with the goal of enabling a memory system for the neural network and therefore allowing it to process data above a single data point but instead entire sequences of data (such as speech).A common LSTM is composed of a cell, an input gate, an output gate and a forget date. The cell is able to remember values over an arbitrary amount of time and the gates control de flow of data in and out of the cell.

<p align='justify'>Although RNNs have a similar learning method as other neural networks they are able to remeber things they learned from prior inputs. In that way, RNNs are able to produce one (or more) output vectors that are not only influenced by the weights applied to the inputs as it is the case with other neural networks, instead their output is also influenced by the context of past inputs and outputs.


<p align="center">
	<img src="https://i.pinimg.com/originals/fe/63/3c/fe633cdec14b8f32adf1c441e37f58dd.gif">
</p>

<p align='justify'>That architecture of time related proccessing makes it easier for them to take part in task such as speech recognition and predictions over time, such as stock opening and/or closing prices.

### About our Roadmap

<p align="justify"> We created a roadmap so that we can describe each step by step we would take to complete the scope established in the project. In addition, we have also established the versioning of our project so that we can have a reference of progress of our process.

![](img/roadmap.png)

## About our Dataset

<p align='justify'>About our dataset, we have created a python script to be able to extract data from APIs that are available on the web, and with the pandas library we can collect this data, as well as determine a period, because the amount of data is very large and therefore not It is so necessary to have exactly everything, and only a portion is needed to present the study.

<p align='justify'>The script consists of consulting the desired API, having as parameter, the start and end period, to make the collection. We select the desired API according to the name reference given by pandas, then present the dataset in order to see if it is correct and finally store the desired data in csv format.


## Our Team

<p align='justify'>Our team is made up of people who are interested in learning more about the financial market and applying this knowledge to deep learning solutions.

| **Name** | **Github** | **E-mail**
|:--:|:---:|:--------:|
Gabrielle Ribeiro | [Gabrielle-Ribeiro](https://github.com/Gabrielle-Ribeiro) | gabrielleribeiro2010@gmail.com |
Danilo Domingo | [danilow200](https://github.com/danilow200) | danilow200@gmail.com |
Alvaro Gouvea | [AlGouvea](https://github.com/AlGouvea) | alvarohsgouvea@gmail.com |
Leonardo Barreiros | [leossb36](https://github.com/leossb36) | leossb36@gmail.com |

### How to Contribute

If you are also interested in the stock market and deep learning, you can contribute to our project by reading our [contribution guide](https://github.com/deeplearningunb/stonks/blob/master/CONTRIBUTING.md) and following our [code of conduct](https://github.com/deeplearningunb/stonks/blob/master/CODE_OF_CONDUCT.md).

## Technologies
The project use the Anaconda Python for your develop.
- Anaconda Python
  - Download [Python3](https://www.python.org/downloads/)
  - Download [Anaconda Python](https://www.anaconda.com/distribution/)
  
If you want config your environment, and have no idea what need to do. We're giving a brief explanation to you [here](ENVIRONMENT.md). 

## Stonks Working

The following graph was generated with the Stonks neural network. It shows the predictions of opening and closing stock prices of Tesla (TSLA) in the last month and also the actual values of this period.

The whole dataset was taken from the Yahoo Finances API.

<p align="center">
  <img src="https://github.com/deeplearningunb/stonks/blob/master/img/graph.png">
</p>

## License

This project is licensed under the terms of the [MIT license](https://github.com/deeplearningunb/stonks/blob/master/LICENSE).
