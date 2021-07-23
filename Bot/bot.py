from aiogram.types.message import Message
from config import TOKEN
import logging
import random
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
logging.basicConfig(level=logging.INFO)


bot = Bot(TOKEN)
dp = Dispatcher(bot)

words_list = ('love', 'death', 'python', 'robot', 'fantasy', 'blizzard', 
              'storm', 'paradise', 'hell', 'heart', 'space', 'loyalty')

class Game(StatesGroup):
    waiting_letter = State()

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_1 = types.KeyboardButton(text="/play")
    keyboard.add(button_1)
    await message.answer('Hello! :)\nSay /play to start a game', reply_markup=keyboard)

@dp.message_handler(commands=['play'])
async def start_game(message: types.Message):
    global lives, selected_word, active_word
    lives = 10
    selected_word = random.choice(words_list)
    active_word = len(selected_word) * '_'

    await message.answer(f'The game is running\nCurrent progress: {active_word}\nLives left: {lives}\n!BloodTrail',
                            reply_markup=types.ReplyKeyboardRemove())
    await message.answer('Input a letter')

    @dp.message_handler()
    async def letter_chosen(message: types.Message, state: FSMContext):
        global lives
        global selected_word
        global active_word
          
        letter = message.text

        while (lives > 0) and ('_' in active_word):
            
            #Checking the entered character
            if (len(letter) > 1) or (letter.isalpha() != True):
                await message.answer('Wrong character entered. Please, input a letter')
                return
            await state.update_data(letter=message.text.lower())

            #Right letter
            if letter.lower() in selected_word:
                index = -1
                await message.answer('There is the letter in the word !SeemsGood')

                while active_word.count(letter) != selected_word.count(letter):
                    index = selected_word.find(letter, index + 1)
                    active_word = active_word[:index] + letter + active_word[index + 1:]
                
                if '_' in active_word:
                    await message.answer(f'Current progress: {active_word}\n!BloodTrail')    

            #False letter
            elif letter.lower() not in selected_word:
                await message.answer('There is no the letter in the word !SMOrc')
                lives -= 1

                if lives > 0:
                    await message.answer(f'Lives left: {lives}\n!BloodTrail')       

            else:
                await message.answer('O_o')

            if ('_' in active_word) and (lives > 0):
                await message.answer('Input another letter')
            
            #Win and finish
            elif lives > 0:
                await message.answer('Congratulations, you won!\n!PogChamp')
                await process_start_command(message)
                
            #Lose and finish    
            elif lives < 1:
                await message.answer('Unfortunately, you lost. !BibleThump\nBetter luck next time')
                await message.answer(f'The word was: {selected_word}')
                await process_start_command(message)

            Game.waiting_letter()
        
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)