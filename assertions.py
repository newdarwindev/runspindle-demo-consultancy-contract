"""Independent business assertions; shared workbook preservation remains in parent."""
def expected(state,fixture):
 value=dict(fixture['expected'])
 return value
def checks(state,fixture,table,actual_rows):
 value={r.get("key"):r.get("value") for r in table}
 return {'code_tests':state.get('tests')=={'rows':10,'expected':10,'passed':True},'issue':state.get('issueStatus')=='Ready for review','one_comment':len(state.get('comments',[]))==1,'hired':state.get('application')=='Hired','pr':state.get('pr') is not None}
