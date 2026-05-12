{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPcJFPb8V5lBof4+qH3NmOA",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/AnushreeKavaloor/genai-2026/blob/main/rock_paper_scissors.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "1ErHscOHIuuG",
        "outputId": "a7d019b1-85b3-47fd-f8ae-6602ab51382a"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter your choice (rock/ paper/scissors): Stone\n",
            "Invalid choice! Please choose rock, paper or scissors\n",
            "Enter your choice (rock/ paper/scissors): Banana\n",
            "Invalid choice! Please choose rock, paper or scissors\n",
            "Enter your choice (rock/ paper/scissors): ROCK\n",
            "Computer choice is paper and yours choice is rock\n",
            "Oops! You lose\n"
          ]
        }
      ],
      "source": [
        "import random\n",
        "game = [\"rock\", \"paper\", \"scissors\"]\n",
        "secret = random.choice(game)\n",
        "while True:\n",
        "    user_choice = input(\"Enter your choice (rock/ paper/scissors): \").lower()\n",
        "    if user_choice not in game:\n",
        "\t    print(\"Invalid choice! Please choose rock, paper or scissors\")\n",
        "    else:\n",
        "\t    break\n",
        "print(\"Computer choice is\", secret, \"and yours choice is\", user_choice)\n",
        "\n",
        "if user_choice == secret:\n",
        "\tprint(\"Tie!\")\n",
        "elif user_choice==\"rock\" and secret==\"scissors\":\n",
        "\tprint(\"You win!\")\n",
        "elif user_choice==\"paper\" and secret==\"rock\":\n",
        "\tprint(\"You win!\")\n",
        "elif user_choice==\"scissors\" and secret==\"paper\":\n",
        "\tprint(\"You win!\")\n",
        "else:\n",
        "\tprint(\"Oops! You lose\")"
      ]
    }
  ]
}