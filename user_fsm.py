from asyncio import sleep

async def user_state_machine(initial_state: str):
    state = initial_state

    while True:
        if state == "registered":
            print("User is registered. Waiting for activation...")
            await sleep(1)  # Симуляция ожидания
            state = "active"

        elif state == "active":
            print("User is active. Performing actions...")
            await sleep(2)  # Симуляция активности
            state = "blocked"

        elif state == "blocked":
            print("User is blocked. Waiting for admin intervention...")
            await sleep(3)  # Симуляция блокировки
            state = "registered"
        else:
            print(f"Unknown state: {state}")
            break
