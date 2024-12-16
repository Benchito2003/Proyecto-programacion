import serial
import time

def read_from_pico(port="/dev/ttyACM0", tiempo=10, baudrate=115200, timeout=1):
    # Configurar el puerto serie
    with serial.Serial(port, baudrate=baudrate, timeout=timeout) as ser:
        print("Conectado a la Pico.")
        ir_data = []

        # Leer datos durante 10 segundos
        start_time = time.time()
        while time.time() - start_time < tiempo:  # Leer por 10 segundos
            line = ser.readline().decode("utf-8").strip()
            if line:
                ir, red = map(int, line.split(","))
                ir_data.append(ir)
                print(f"IR: {ir}, Red: {red}")

        return ir_data

def calculate_heart_rate(ir_data, sampling_rate=10):
    # Calcular frecuencia cardíaca (igual al módulo anterior)
    peaks = []
    threshold = sum(ir_data) / len(ir_data)
    for i in range(1, len(ir_data) - 1):
        if ir_data[i] > ir_data[i - 1] and ir_data[i] > ir_data[i + 1] and ir_data[i] > threshold:
            peaks.append(i)
    intervals = [(peaks[i + 1] - peaks[i]) / sampling_rate for i in range(len(peaks) - 1)]
    if len(intervals) == 0:
        return 0
    avg_interval = sum(intervals) / len(intervals)
    return round(60 / avg_interval)

def obtener_frecuencia(time):
    ir_data = read_from_pico(port="/dev/ttyACM0", tiempo=time)
    frecuencia = calculate_heart_rate(ir_data)
    return frecuencia

if __name__ == "__main__":
    # Leer datos y calcular BPM
    ir_data = read_from_pico(port="/dev/ttyACM0")  # Cambia "COM3" por el puerto de tu Pico
    bpm = calculate_heart_rate(ir_data)
    print(f"Frecuencia cardíaca: {bpm} BPM")
    print (type(bpm))
