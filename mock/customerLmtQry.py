# coding=utf-8
from flask import Flask, jsonify, request


dict_count = {
    "customerLmtQry_count": 0,
    "loanTrial_count": 0,
    "loanWithdrawAply_count": 0,
    "loanWithdrawRstQry_count": 0,
    "repayPlanQry_count": 0,
    "generalRepayment_count": 0,
    "repayRstQry_count": 0,
    "elyRepayTrial_count": 0,
    "CrdtApplyAcns_count": 0,
    "crdtRestQry_count": 0,
    "chgBankCardCFC_count": 0

}

# 1.南京银行额度查询 customerLmtQry
customerLmtQry_params = {
    "rspData": {
        "AprvPasTmStmp": "20190305",
        "AvaCrdtGrntLmt": "13900.82",
        "CrdtGrntLmt": "50000",
        "IdCode": "341126197709218382",
        "BillAmt": "22699.18"
    },
    "rspHead": {
        "returnCode": "000000",
        "returnMsg": "交易成功",
        "transTime": "095249070",
        "seqNo": "ANX7702609379112596783882435",
        "transDate": "20190410",
        "serviceID": "customerLmtQry",
        "channelID": "LTXJD"
    }
}

# 2.借款试算：借款页面的试算数据展示 loanTrial
loanTrial_params = {
    "rspData": {
        "Interest": "18.3",
        "repayPlan": [
            {
                "CrntInt": "9.0",
                "RpymtDt": "20190510",
                "CrntRpymtAmt": "206.03",
                "Principal": "197.03",
                "CrntNum": "1"
            },
            {
                "CrntInt": "6.25",
                "RpymtDt": "20190610",
                "CrntRpymtAmt": "206.03",
                "Principal": "199.78",
                "CrntNum": "2"
            },
            {
                "CrntInt": "3.05",
                "RpymtDt": "20190710",
                "CrntRpymtAmt": "206.24",
                "Principal": "203.19",
                "CrntNum": "3"
            }
        ],
        "RtType": "Y",
        "LoanPrdNum": "3",
        "RpymtTotAmt": "618.3",
        "Rate": "0.18",
        "FrstRpymtDt": "20190510",
        "LstRpymtDt": "20190710"
    },
    "rspHead": {
        "returnCode": "7001",
        "returnMsg": "CFC借款试算成功",
        "transTime": "140556376",
        "seqNo": "ANX7854482447452593975696285",
        "transDate": "20190410",
        "serviceID": "loanTrial",
        "channelID": "LTXJD"
    }
}

# 3.借款申请 loanWithdrawAply
loanWithdrawAply_params = {
    "rspData": {
        "TranDealSt": "PRO",
        "LoanAppSeqNo": "ASIB20190401165853"
    },
    "rspHead": {
        "returnCode": "000000",
        "returnMsg": "交易成功",
        "transTime": "170516013",
        "seqNo": "ANX186078809332591409533452",
        "transDate": "20190401",
        "serviceID": "loanWithdrawAply",
        "channelID": "LTXJD"
    }
}

# 4.放款结果查询 loanWithdrawRstQry
loanWithdrawRstQry_params = {
    "rspData": {
        "DstrState": "SUC",
        "LoanInfData": "{\"amount\":\"700\",\"loanBillNum\":\"99990120600000002015415\",\"dealTime\":\"20190415161102\",\"requestTime\":\"20190415161029\",\"loanTime\":\"20190401161102\", \"signStatus\":\"UNT\",\"authNum\":\"091B0006\",\"serialNum\":\"wopxjdASIB20190415165502\",\"bankAccount\":\"9559981700000000035\"}"
    },
    "rspHead": {
        "returnCode": "000000",
        "returnMsg": "交易成功",
        "transTime": "164500056",
        "seqNo": "ANX186078809332591409533452",
        "transDate": "20190401",
        "serviceID": "loanWithdrawRstQry",
        "channelID": "LTXJD"
    }
}

# 5.还款计划查询 repayPlanQry

# currentstarus: 0--正常, 1--逾期, 2--呆滞, 3--呆账, 4--核销, 5--结清, 6--不还

repayPlanQry_params = {
    "rspData": {
        "TranDealSt": "SUC",
        "RpymtInfData": "[{\"billAmt\":700.58,\"carryInterestDate\":\"2018-04-04\",\"chargeOffInterest\":0,\"chargeOffPrincl\":0,\"currentTerm\":1,\"custName\":\"马小花\",\"interestRateFlag\":\"Y\",\"loanAccountStatus\":\"0\",\"loanBillNum\":\"99990120600000002015415\",\"normalPrincl\":700.00,\"repayMode\":\"3\",\"repaymentPlanSubDtos\":[{\"beginDate\":\"2018-04-04\",\"compoundInterest\":0.05,\"currentStatus\":\"0\",\"currentTerm\":1,\"debitInterest\":0.06,\"defaultInterest\":0.07,\"endDate\":\"2018-05-10\",\"graceEndDate\":\"2018-05-13\",\"initInterest\":0.08,\"initPrincl\":233.33,\"shouldCompoundInterest\":0.09,\"shouldDefaultInterest\":0.10,\"shouldInterest\":0.10,\"shouldPrincl\":233.33,\"termRepayTotalAmt\":238.88},{\"beginDate\":\"2018-05-10\",\"compoundInterest\":0.11,\"currentStatus\":\"0\",\"currentTerm\":2,\"debitInterest\":0.12,\"defaultInterest\":0.13,\"endDate\":\"2018-06-10\",\"graceEndDate\":\"2018-06-13\",\"initInterest\":0.14,\"initPrincl\":233.33,\"shouldCompoundInterest\":0.15,\"shouldDefaultInterest\":0.16,\"shouldInterest\":0.17,\"shouldPrincl\":233.33,\"termRepayTotalAmt\":238.88},{\"beginDate\":\"2018-06-10\",\"compoundInterest\":0.18,\"currentStatus\":\"0\",\"currentTerm\":3,\"debitInterest\":0.19,\"defaultInterest\":0.20,\"endDate\":\"2018-07-10\",\"graceEndDate\":\"2018-07-13\",\"initInterest\":0.21,\"initPrincl\":233.34,\"shouldCompoundInterest\":0.22,\"shouldDefaultInterest\":0.23,\"shouldInterest\":0.24,\"shouldPrincl\":233.34,\"termRepayTotalAmt\":239.99}],\"serialNum\":\"wopxjdASIB20190415165502\",\"termRepayPrincl\":233.33,\"termRepayTotalAmt\":233.88,\"terminateDate\":\"2018-07-10\",\"totalTerm\":3}]"
    },
    "rspHead": {
        "returnCode": "000000",
        "returnMsg": "交易成功",
        "transTime": "230128518",
        "seqNo": "ANX186078809332591409533452",
        "transDate": "164500056",
        "serviceID": "repayPlanQry",
        "channelID": "LTXJD"
    }
}

# repayPlanQry_params = {
# 	"rspData": {
# 		"TranDealSt": "SUC",
# 		"RpymtInfData": [{
# 			"billAmt": 0,
# 			"carryInterestDate": "2019-04-24",
# 			"chargeOffInterest": 0,
# 			"chargeOffPrincl": 0,
# 			"currentTerm": 1,
# 			"custName": "王举",
# 			"interestRateFlag": "Y",
# 			"loanAccountStatus": "5",
# 			"loanBillNum": "99990120600000002015415",
# 			"normalPrincl": 0,
# 			"repayMode": "3",
# 			"repaymentPlanSubDtos": [{
# 				"beginDate": "2019-04-24",
# 				"compoundInterest": 0,
# 				"currentStatus": "5",
# 				"currentTerm": 1,
# 				"debitInterest": 0,
# 				"defaultInterest": 0,
# 				"endDate": "2019-05-10",
# 				"graceEndDate": "2019-05-13",
# 				"initInterest": 0.5,
# 				"initPrincl": 1000,
# 				"shouldCompoundInterest": 0,
# 				"shouldDefaultInterest": 0,
# 				"shouldInterest": 0,
# 				"shouldPrincl": 0,
# 				"termRepayTotalAmt": 1000.5
# 			}],
# 			"serialNum": "wopxjdASIB20190426172520",
# 			"termRepayPrincl": 0,
# 			"termRepayTotalAmt": 0,
# 			"terminateDate": "2019-07-24",
# 			"totalTerm": 1
# 		}]
# 	},
# 	"rspHead": {
# 		"returnCode": "000000",
# 		"returnMsg": "交易成功",
# 		"transTime": "180242619",
# 		"seqNo": "ANX890090453422369502880286088",
# 		"transDate": "20190426",
# 		"serviceID": "repayPlanQry",
# 		"channelID": "LTXJD"
# 	}
# }

# 6.还款接口 generalRepayment
generalRepayment_params = {
    "rspData": {
        "TranDealSt": "SUC"
    },
    "rspHead": {
        "returnCode": "7001",
        "returnMsg": "还款提交成功",
        "transTime": "013905966",
        "seqNo": "ANX86696771931723654285097662",
        "transDate": "20180819",
        "serviceID": "generalRepayment",
        "channelID": "LTXJD"
    }
}

# 7.客户还款结果查询 repayRstQry
# retcode： 7001 SUC # 6001 FAI # 5001 ERR
repayRstQry_params = {
	"rspData": {
		"TranDealSt": "F",
		"ClientName": "",
		"RpymtInfData": "{\"dataSource\":\"XSHK\",\"dkjiejuh\":\"99990120600000002015415\",\"ghyqlxfx\":0.00,\"huankDate\":\"20190711\",\"repaySerialNumber\":\"wopxjd1149271645742714880\",\"repayStatus\":\"F\",\"term\":\"1\"}",
		"IdCode": ""
	},
	"rspHead": {
		"returnCode": "6001",
		"returnMsg": "交易失败，借方账户余额不足[PB520011-01]",
		"transTime": "190000228",
		"seqNo": "ANX955788985224370900417213930",
		"transDate": "20190711",
		"serviceID": "repayRstQry",
		"channelID": "LTXJD"
	}
}

# 8.提前还款试算 elyRepayTrial
elyRepayTrial_params = {
    "rspData": {
        "TranDealSt": "SUC",
        "DfltAmt": "2.88",
        "RpymtTotAmt": "712.33",
        "DeductAmt": "708.88",
        "DscntIntAmt": "0.88",
        "Interest": "0.99",
        "ClientName": "马小花",
        "ContractNo": "NJCB1117712900408795136",
        "RpymtInfData": "{\"RepayTerm\":\"\",\"CompoundInt\":\"0.33\"}",
        "OdueInt": "0.44",
        "DueBillNo": "99990120600000002015415",
        "OduePrcpl": "536.66",
        "IdCode": "341126197709218382",
        "Principal": "700"
    },
    "rspHead": {
        "returnCode": "000000",
        "returnMsg": "提前还款试算成功",
        "transTime": "162226567",
        "seqNo": "ANX7936384355672592462420398",
        "transDate": "20190417",
        "serviceID": "elyRepayTrial",
        "channelID": "LTXJD"
    }
}

# 9.获信申请
CrdtApplyAcns_params = {
    "rspData": {
        "CrdtAppSeqNo": "1120692328708734976",
        "TranDealSt": "PRO",
        "SysRspTmStmp": "20190423221407"
    },
    "rspHead": {
        "returnCode": "000000",
        "returnMsg": "交易成功",
        "transTime": "221407270",
        "seqNo": "ANX887649299928427125800056972",
        "transDate": "20190423",
        "serviceID": "CrdtApplyAcns",
        "channelID": "LTXJD"
    }
}

# 10.授信结果查询 //当前为失败，需要改returncode 为000000
crdtRestQry_params = {
    "rspData": {
        "CrdtAppSeqNo": "wopxjd1120692328708734976",
        "ClientName": "李雪",
        "CrdtFnlDcsnFlg": "DEC",
        "CrdtGrntLmt": "",
        "AuthNo": "113B26GU",
        "CrdtStrtTmStmp": "20190423221500",
        "CrdtEndTmStmp": "20990101240000",
        "CrdtAppData": "{\"rate\":\"18\",\"idNum\":\"320722199112030522\",\"applyTime\":\"20190423221500\",\"checkTime\":\"\",\"autoNumber\":\"113B26GU\"}"
    },
    "rspHead": {
        "returnCode": "111111",
        "returnMsg": "交易成功",
        "transTime": "221505041",
        "seqNo": "ANX887650033352988327458644715",
        "transDate": "20190423",
        "serviceID": "crdtRestQry",
        "channelID": "LTXJD"
    }
}

# 11.更换银行卡接口返回
chgBankCardCFC_params = {
    "rspData": {
        "TranDealSt": "1",
        "ErrCode": "000000",
    },
    "rspHead": {
        "returnCode": "000000",
        "returnMsg": "交易成功",
        "transTime": "221505041",
        "seqNo": "ANX887650033352988327458644715",
        "transDate": "20190423",
        "serviceID": "chgBankCardCFC",
        "channelID": "LTXJD"
    }
}

app = Flask(__name__)


# 1.南京银行额度查询 customerLmtQry
@app.route('/customerLmtQry', methods=['POST'])
def customerLmtQry():
    if request.method == 'POST':
        dict_count["customerLmtQry_count"] += 1
        return jsonify(customerLmtQry_params)


# 2.借款试算：借款页面的试算数据展示 loanTrial
@app.route('/loanTrial', methods=['POST'])
def loanTrial():
    if request.method == 'POST':
        dict_count["loanTrial_count"] += 1
        return jsonify(loanTrial_params)


# 3.借款申请 loanWithdrawAply
@app.route('/loanWithdrawAply', methods=['POST'])
def loanWithdrawAply():
    if request.method == 'POST':
        dict_count["loanWithdrawAply_count"] += 1
        return jsonify(loanWithdrawAply_params)


# 4.放款结果查询 loanWithdrawRstQry
@app.route('/loanWithdrawRstQry', methods=['POST'])
def loanWithdrawRstQry():
    if request.method == 'POST':
        dict_count["loanWithdrawRstQry_count"] += 1
        return jsonify(loanWithdrawRstQry_params)


# 5.还款计划查询 repayPlanQry
@app.route('/repayPlanQry', methods=['POST'])
def repayPlanQry():
    if request.method == 'POST':
        dict_count["repayPlanQry_count"] += 1
        return jsonify(repayPlanQry_params)


# 6.还款接口 generalRepayment
@app.route('/generalRepayment', methods=['POST'])
def generalRepayment():
    if request.method == 'POST':
        dict_count["generalRepayment_count"] += 1
        return jsonify(generalRepayment_params)


# 7.客户还款结果查询 repayRstQry
@app.route('/repayRstQry', methods=['POST'])
def repayRstQry():
    if request.method == 'POST':
        dict_count["repayRstQry_count"] += 1
        return jsonify(repayRstQry_params)


# 8.提前还款试算 elyRepayTrial
@app.route('/elyRepayTrial', methods=['POST'])
def elyRepayTrial():
    if request.method == 'POST':
        dict_count["elyRepayTrial_count"] += 1
        return jsonify(elyRepayTrial_params)


# 9.获信申请返回 CrdtApplyAcns
@app.route('/CrdtApplyAcns', methods=['POST'])
def CrdtApplyAcns():
    if request.method == 'POST':
        dict_count["CrdtApplyAcns_count"] += 1
        return jsonify(CrdtApplyAcns_params)


# 10.获信申请返回 crdtRestQry
@app.route('/crdtRestQry', methods=['POST'])
def crdtRestQry():
    if request.method == 'POST':
        dict_count["crdtRestQry_count"] += 1
        return jsonify(crdtRestQry_params)


# 11.绑卡结果查询 chgBankCardCFC
@app.route('/chgBankCardCFC', methods=['POST'])
def chgBankCardCFC():
    if request.method == 'POST':
        dict_count["chgBankCardCFC_count"] += 1
        return jsonify(chgBankCardCFC_params)


# 12.调用次数统计 trigger_count
@app.route('/trigger_count', methods=['POST'])
def trigger_count():
    if request.method == 'POST':
        return jsonify(dict_count)


if __name__ == '__main__':
    try:
        print("Mock is running.....")
        app.run(host='0.0.0.0', debug=True)
    except Exception as err:
        print(err)
    finally:
        print("\nERROR!!! Press Enter to exit......")
