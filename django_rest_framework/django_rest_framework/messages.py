from rest_framework.response import Response


def failure(error_code, error_message):
    return Response({"error": {"code": error_code, "message": error_message}, "success": "false"},
                    error_code)


def success(status_code, data):
    return Response({"data": data, "success": "true"}, status=status_code)


def empty_success(status_code):
    return Response({'success': 'true'},
                    status_code)


def message_from_errors(errors):
    return "".join(list(errors.values())[0])
