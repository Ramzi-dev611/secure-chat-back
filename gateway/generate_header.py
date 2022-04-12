import kerberos


def get_header():
    _, krb_context = kerberos.authGSSClientInit("host@service.securechat.tn", "host/client.securechat.tn@SECURECHAT.TN")
    print("step : " + str(kerberos.authGSSClientStep(krb_context, "")))

    print("Creating auth header......")
    negotiate_details = kerberos.authGSSClientResponse(krb_context)
    headers = {"Authorization": "Negotiate " + negotiate_details}
    return headers
