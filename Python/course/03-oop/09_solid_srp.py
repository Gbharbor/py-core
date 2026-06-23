# SOLID -> S = Single Responsibility Principle (SRP)

# Definition:
# A class should have only ONE responsibility,
# meaning it should have only ONE reason to change.
#
# When a class performs multiple unrelated tasks,
# it becomes harder to maintain, test, and reuse.


# WRONG EXAMPLE

class FinancialReport:
    def calculate_data(self, data):
        # Responsible for data processing
        pass

    def save_file(self):
        # Responsible for file management
        pass

    def send_email(self, email):
        # Responsible for email delivery
        pass


# Problem:
#
# This class has 3 responsibilities:
# 1. Process data
# 2. Save files
# 3. Send emails
#
# If any of these functionalities change,
# the class must be modified.
#
# This violates the Single Responsibility Principle.


# CORRECT EXAMPLE

class FinancialReport:
    def calculate_data(self, data):
        # Responsible only for processing
        # and generating report data
        return data


class ReportFileManager:
    def save_report(self, report):
        # Responsible only for saving reports
        print("Report saved successfully!")


class ReportSender:
    def send_email(self, report):
        # Responsible only for sending reports
        print("Report sent successfully!")


# USING THE CLASSES

report = FinancialReport()
report_file = ReportFileManager()
report_sender = ReportSender()

ready_report = report.calculate_data("Financial Data")

report_file.save_report(ready_report)
report_sender.send_email(ready_report)
