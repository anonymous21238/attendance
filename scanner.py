import cv2
import datetime
import sqlite3
import os

def scan_qr_and_record():
    # Initialize camera
    cap = cv2.VideoCapture(0)
    
    # Initialize QR code detector
    detector = cv2.QRCodeDetector()

    while True:
        _, img = cap.read()
        
        # Detect and decode
        data, bbox, _ = detector.detectAndDecode(img)
        
        # If there is a QR code
        if bbox is not None and data:
            print("Scanned Data:", data) # data is the roll number in this case
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            # Insert into database
            conn = sqlite3.connect('Database\\attendance.db')
            c = conn.cursor()
            c.execute("INSERT INTO attendance VALUES (?, ?, ?)", (datetime.datetime.now().date(), data, timestamp))
            conn.commit()
            conn.close()
            
            print(f"Attendance recorded for roll number: {data} at {timestamp}")
            
            # Break after scanning the required QR code
            break
            
        # Display the resulting frame
        cv2.imshow('QR Code Scanner', img)
        
        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Run the scanning function
scan_qr_and_record()