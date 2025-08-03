from enum import Enum


class CSVExportStatus(Enum):
    PENDING = 1
    PROCESSING = 2
    SUCCESS = 3
    FAILURE = 4


def get_csv_status(status, data):
    # Use a match case statement to select the correct response depending on the status of the export operation
    match (status, data):
        case (CSVExportStatus.PENDING, _):
            # return a tuple with the string "Pending..." and the data converted from a list of lists of anything, to a list of lists of strings.
            # nested map
            # convert from a map object back into a list.
            return ("Pending...", list(map(lambda x: list(map(str, x)), data)))
        case (CSVExportStatus.PROCESSING, _):
            # return a tuple with the string "Processing..." and the data converted from a list of lists of strings into one string in CSV format.
            # For each row string, combine the strings with join with newlines "\n" inbetween to form a table.
            return ("Processing...", '\n'.join(','.join(row) for row in data))
        case (CSVExportStatus.SUCCESS, _):
            # return a tuple with the string "Success!" and simply return the data as is.
            return ("Success!", data)
        case (CSVExportStatus.FAILURE, _):
            # the data after it has been prepared 
            processed = list(map(lambda x: list(map(str, x)), data))
            # return a tuple with the string "Unknown error, retrying..." and 
            # and processed into a CSV string
            return ("Unknown error, retrying...", '\n'.join(','.join(row) for row in processed))
        case _:
            raise Exception("unknown export status")