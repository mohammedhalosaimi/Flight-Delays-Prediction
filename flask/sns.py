import boto3

class Sns:

    def sendSMS(self, PhoneNumber, result):
        # Create an SNS client
        sns = boto3.client(
            "sns",
            aws_access_key_id="AKIAJ4Z2D5LPUTXQYU3A",
            aws_secret_access_key="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",
            region_name="us-east-1"
        )
        # try and send the message
        try:

            # Send a SMS message to the specified phone number
            response = sns.publish(
                PhoneNumber=PhoneNumber,
                Message=result)

        # except if message can't be sent
        except:
            print("Something went wrong. can't send a text message!")
            pass

        # Print out the response
        # print(response)

# snsService = Sns()
# snsService.sendSMS('+61466636990', 'Hello Mohammed')