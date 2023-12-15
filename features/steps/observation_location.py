from behave import given, when, then

@given(u'the observing date is "2023-12-14 22:00:00"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given the observing date is "2023-12-14 22:00:00"')

@given(u'the latitude is 40.7128 degree')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given the latitude is 40.7128 degree')


@given(u'the longitude is -74.0060 degree')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given the longitude is -74.0060 degree')

@when(u'the user asks for observation parameters')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the user asks for observation parameters')

@then(u'the date is "2023-12-14"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the date is "2023-12-14"')

@then(u'the time is "22:00:00"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the time is "22:00:00"')

@then(u'the latitude is 40.7128 degree')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the latitude is 40.7128 degree')

@then(u'the longitude is -74.0060 degree')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the longitude is -74.0060 degree')

