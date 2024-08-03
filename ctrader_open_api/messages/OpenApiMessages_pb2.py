# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: OpenApiMessages.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor, descriptor_pool as _descriptor_pool, \
    symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x15OpenApiMessages.proto\x1a\x1aOpenApiModelMessages.proto\"\x8c\x01\n\x19ProtoOAApplicationAuthReq\x12G\n\x0bpayloadType\x18\x01 \x01(\x0e\x32\x13.ProtoOAPayloadType:\x1dPROTO_OA_APPLICATION_AUTH_REQ\x12\x10\n\x08\x63lientId\x18\x02 \x02(\t\x12\x14\n\x0c\x63lientSecret\x18\x03 \x02(\t\"d\n\x19ProtoOAApplicationAuthRes\x12G\n\x0bpayloadType\x18\x01 \x01(\x0e\x32\x13.ProtoOAPayloadType:\x1dPROTO_OA_APPLICATION_AUTH_RES\"\x8e\x01\n\x15ProtoOAAccountAuthReq\x12\x43\n\x0bpayloadType\x18\x01 \x01(\x0e\x32\x13.ProtoOAPayloadType:\x19PROTO_OA_ACCOUNT_AUTH_REQ\x12\x1b\n\x13\x63tidTraderAccountId\x18\x02 \x02(\x03\x12\x13\n\x0b\x61\x63\x63\x65ssToken\x18\x03 \x02(\t\"y\n\x15ProtoOAAccountAuthRes\x12\x43\n\x0bpayloadType\x18\x01 \x01(\x0e\x32\x13.ProtoOAPayloadType:\x19PROTO_OA_ACCOUNT_AUTH_RES\x12\x1b\n\x13\x63tidTraderAccountId\x18\x02 \x02(\x03\"\xb5\x01\n\x0fProtoOAErrorRes\x12<\n\x0bpayloadType\x18\x01 \x01(\x0e\x32\x13.ProtoOAPayloadType:\x12PROTO_OA_ERROR_RES\x12\x1b\n\x13\x63tidTraderAccountId\x18\x02 \x01(\x03\x12\x11\n\terrorCode\x18\x03 \x02(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\x1f\n\x17maintenanceEndTimestamp\x18\x05 \x01(\x03\"z\n\x1cProtoOAClientDisconnectEvent\x12J\n\x0bpayloadType\x18\x01 \x01(\x0e\x32\x13.ProtoOAPayloadType: PROTO_OA_CLIENT_DISCONNECT_EVENT\x12\x0e\n\x06reason\x18\x02 \x01(\t\"\xa9\x01\n$ProtoOAAccountsTokenInvalidatedEvent\x12S\n\x0bpayloadType\x18\x01 \x01(\x0e\x32\x13.ProtoOAPayloadType:)PROTO_OA_ACCOUNTS_TOKEN_INVALIDATED_EVENT\x12\x1c\n\x14\x63tidTraderAccountIds\x18\x02 \x03(\x03\x12\x0e\n\x06reason\x18\x03 \x01(\t\"S\n\x11ProtoOAVersionReq\x12>\n\x0bpayloadType\x18\x01 \x01(\x0e\x32\x13.ProtoOAPayloadType:\x14PROTO_OA_VERSION_REQ\"d\n\x11ProtoOAVersionRes\x12>\n\x0bpayloadType\x18\x01 \x01(\x0e\x32\x13.ProtoOAPayloadType:\x14PROTO_OA_VERSION_RES\x12\x0f\n\x07version\x18\x02 \x02(\t\"\xb1\x05\n\x12ProtoOANewOrderReq\x12@\n\x0bpayloadType\x18\x01 \x01(\x0e\x32\x13.ProtoOAPayloadType:\x16PROTO_OA_NEW_ORDER_REQ\x12\x1b\n\x13\x63tidTraderAccountId\x18\x02 \x02(\x03\x12\x10\n\x08symbolId\x18\x03 \x02(\x03\x12$\n\torderType\x18\x04 \x02(\x0e\x32\x11.ProtoOAOrderType\x12$\n\ttradeSide\x18\x05 \x02(\x0e\x32\x11.ProtoOATradeSide\x12\x0e\n\x06volume\x18\x06 \x02(\x03\x12\x12\n\nlimitPrice\x18\x07 \x01(\x01\x12\x11\n\tstopPrice\x18\x08 \x01(\x01\x12:\n\x0btimeInForce\x18\t \x01(\x0e\x32\x13.ProtoOATimeInForce:\x10GOOD_TILL_CANCEL\x12\x1b\n\x13\x65xpirationTimestamp\x18\n \x01(\x03\x12\x10\n\x08stopLoss\x18\x0b \x01(\x01\x12\x12\n\ntakeProfit\x18\x0c \x01(\x01\x12\x0f\n\x07\x63omment\x18\r \x01(\t\x12\x19\n\x11\x62\x61seSlippagePrice\x18\x0e \x01(\x01\x12\x18\n\x10slippageInPoints\x18\x0f \x01(\x05\x12\r\n\x05label\x18\x10 \x01(\t\x12\x12\n\npositionId\x18\x11 \x01(\x03\x12\x15\n\rclientOrderId\x18\x12 \x01(\t\x12\x18\n\x10relativeStopLoss\x18\x13 \x01(\x03\x12\x1a\n\x12relativeTakeProfit\x18\x14 \x01(\x03\x12\x1a\n\x12guaranteedStopLoss\x18\x15 \x01(\x08\x12\x18\n\x10trailingStopLoss\x18\x16 \x01(\x08\x12<\n\x11stopTriggerMethod\x18\x17 \x01(\x0e\x32\x1a.ProtoOAOrderTriggerMethod:\x05TRADE\"\x9c\x03\n\x15ProtoOAExecutionEvent\x12\x42\n\x0bpayloadType\x18\x01 \x01(\x0e\x32\x13.ProtoOAPayloadType:\x18PROTO_OA_EXECUTION_EVENT\x12\x1b\n\x13\x63tidTraderAccountId\x18\x02 \x02(\x03\x12,\n\rexecutionType\x18\x03 \x02(\x0e\x32\x15.ProtoOAExecutionType\x12\"\n\x08position\x18\x04 \x01(\x0b\x32\x10.ProtoOAPosition\x12\x1c\n\x05order\x18\x05 \x01(\x0b\x32\r.ProtoOAOrder\x12\x1a\n\x04\x64\x65\x61l\x18\x06 \x01(\x0b\x32\x0c.ProtoOADeal\x12:\n\x14\x62onusDepositWithdraw\x18\x07 \x01(\x0b\x32\x1c.ProtoOABonusDepositWithdraw\x12\x30\n\x0f\x64\x65positWithdraw\x18\x08 \x01(\x0b\x32\x17.ProtoOADepositWithdraw\x12\x11\n\terrorCode\x18\t \x01(\t\x12\x15\n\risServerEvent\x18\n \x01(\x08\"\x8a\x01\n\x15ProtoOACancelOrderReq\x12\x43\n\x0bpayloadType\x18\x01 \x01(\x0e\x32\x13.ProtoOAPayloadType:\x19PROTO_OA_CANCEL_ORDER_REQ\x12\x1b\n\x13\x63tidTraderAccountId\x18\x02 \x02(\x03\x12\x0f\n\x07orderId\x18\x03 \x02(\x03\"\xc6\x03\n\x14ProtoOAAmendOrderReq\x12\x42\n\x0bpayloadType\x18\x01 \x01(\x0e\x32\x13.ProtoOAPayloadType:\x18PROTO_OA_AMEND_ORDER_REQ\x12\x1b\n\x13\x63tidTraderAccountId\x18\x02 \x02(\x03\x12\x0f\n\x07orderId\x18\x03 \x02(\x03\x12\x0e\n\x06volume\x18\x04 \x01(\x03\x12\x12\n\nlimitPrice\x18\x05 \x01(\x01\x12\x11\n\tstopPrice\x18\x06 \x01(\x01\x12\x1b\n\x13\x65xpirationTimestamp\x18\x07 \x01(\x03\x12\x10\n\x08stopLoss\x18\x08 \x01(\x01\x12\x12\n\ntakeProfit\x18\t \x01(\x01\x12\x18\n\x10slippageInPoints\x18\n \x01(\x05\x12\x18\n\x10relativeStopLoss\x18\x0b \x01(\x03\x12\x1a\n\x12relativeTakeProfit\x18\x0c \x01(\x03\x12\x1a\n\x12guaranteedStopLoss\x18\r \x01(\x08\x12\x18\n\x10trailingStopLoss\x18\x0e \x01(\x08\x12<\n\x11stopTriggerMethod\x18\x0f \x01(\x0e\x32\x1a.ProtoOAOrderTriggerMethod:\x05TRADE\"\xb8\x02\n\x1bProtoOAAmendPositionSLTPReq\x12J\n\x0bpayloadType\x18\x01 \x01(\x0e\x32\x13.ProtoOAPayloadType: PROTO_OA_AMEND_POSITION_SLTP_REQ\x12\x1b\n\x13\x63tidTraderAccountId\x18\x02 \x02(\x03\x12\x12\n\npositionId\x18\x03 \x02(\x03\x12\x10\n\x08stopLoss\x18\x04 \x01(\x01\x12\x12\n\ntakeProfit\x18\x05 \x01(\x01\x12\x1a\n\x12guaranteedStopLoss\x18\x07 \x01(\x08\x12\x18\n\x10trailingStopLoss\x18\x08 \x01(\x08\x12@\n\x15stopLossTriggerMethod\x18\t \x01(\x0e\x32\x1a.ProtoOAOrderTriggerMethod:\x05TRADE\"\xa1\x01\n\x17ProtoOAClosePositionReq\x12\x45\n\x0bpayloadType\x18\x01 \x01(\x0e\x32\x13.ProtoOAPayloadType:\x1bPROTO_OA_CLOSE_POSITION_REQ\x12\x1b\n\x13\x63tidTraderAccountId\x18\x02 \x02(\x03\x12\x12\n\npositionId\x18\x03 \x02(\x03\x12\x0e\n\x06volume\x18\x04 \x02(\x03\"\xe2\x01\n\x1dProtoOATrailingSLChangedEvent\x12L\n\x0bpayloadType\x18\x01 \x01(\x0e\x32\x13.ProtoOAPayloadType:\"PROTO_OA_TRAILING_SL_CHANGED_EVENT\x12\x1b\n\x13\x63tidTraderAccountId\x18\x02 \x02(\x03\x12\x12\n\npositionId\x18\x03 \x02(\x03\x12\x0f\n\x07orderId\x18\x04 \x02(\x03\x12\x11\n\tstopPrice\x18\x05 \x02(\x01\x12\x1e\n\x16utcLastUpdateTimestamp\x18\x06 \x02(\x03\"u\n\x13ProtoOAAssetListReq\x12\x41\n\x0bpayloadType\x18\x01 \x01(\x0e\x32\x13.ProtoOAPayloadType:\x17PROTO_OA_ASSET_LIST_REQ\x12\x1b\n\x13\x63tidTraderAccountId\x18\x02 \x02(\x03\"\x93\x01\n\x13ProtoOAAssetListRes\x12\x41\n\x0bpayloadType\x18\x01 \x01(\x0e\x32\x13.ProtoOAPayloadType:\x17PROTO_OA_ASSET_LIST_RES\x12\x1b\n\x13\x63tidTraderAccountId\x18\x02 \x02(\x03\x12\x1c\n\x05\x61sset\x18\x03 \x03(\x0b\x32\r.ProtoOAAsset\"\xa0\x01\n\x15ProtoOASymbolsListReq\x12\x43\n\x0bpayloadType\x18\x01 \x01(\x0e\x32\x13.ProtoOAPayloadType:\x19PROTO_OA_SYMBOLS_LIST_REQ\x12\x1b\n\x13\x63tidTraderAccountId\x18\x02 \x02(\x03\x12%\n\x16includeArchivedSymbols\x18\x03 \x01(\x08:\x05\x66\x61lse\"\xce\x01\n\x15ProtoOASymbolsListRes\x12\x43\n\x0bpayloadType\x18\x01 \x01(\x0e\x32\x13.ProtoOAPayloadType:\x19PROTO_OA_SYMBOLS_LIST_RES\x12\x1b\n\x13\x63tidTraderAccountId\x18\x02 \x02(\x03\x12#\n\x06symbol\x18\x03 \x03(\x0b\x32\x13.ProtoOALightSymbol\x12.\n\x0e\x61rchivedSymbol\x18\x04 \x03(\x0b\x32\x16.ProtoOAArchivedSymbol\"\x8a\x01\n\x14ProtoOASymbolByIdReq\x12\x43\n\x0bpayloadType\x18\x01 \x01(\x0e\x32\x13.ProtoOAPayloadType:\x19PROTO_OA_SYMBOL_BY_ID_REQ\x12\x1b\n\x13\x63tidTraderAccountId\x18\x02 \x02(\x03\x12\x10\n\x08symbolId\x18\x03 \x03(\x03\"\xc8\x01\n\x14ProtoOASymbolByIdRes\x12\x43\n\x0bpayloadType\x18\x01 \x01(\x0e\x32\x13.ProtoOAPayloadType:\x19PROTO_OA_SYMBOL_BY_ID_RES\x12\x1b\n\x13\x63tidTraderAccountId\x18\x02 \x02(\x03\x12\x1e\n\x06symbol\x18\x03 \x03(\x0b\x32\x0e.ProtoOASymbol\x12.\n\x0e\x61rchivedSymbol\x18\x04 \x03(\x0b\x32\x16.ProtoOAArchivedSymbol\"\xb7\x01\n\x1eProtoOASymbolsForConversionReq\x12M\n\x0bpayloadType\x18\x01 \x01(\x0e\x32\x13.ProtoOAPayloadType:#PROTO_OA_SYMBOLS_FOR_CONVERSION_REQ\x12\x1b\n\x13\x63tidTraderAccountId\x18\x02 \x02(\x03\x12\x14\n\x0c\x66irstAssetId\x18\x03 \x02(\x03\x12\x13\n\x0blastAssetId\x18\x04 \x02(\x03\"\xb1\x01\n\x1eProtoOASymbolsForConversionRes\x12M\n\x0bpayloadType\x18\x01 \x01(\x0e\x32\x13.ProtoOAPayloadType:#PROTO_OA_SYMBOLS_FOR_CONVERSION_RES\x12\x1b\n\x13\x63tidTraderAccountId\x18\x02 \x02(\x03\x12#\n\x06symbol\x18\x03 \x03(\x0b\x32\x13.ProtoOALightSymbol\"\x93\x01\n\x19ProtoOASymbolChangedEvent\x12G\n\x0bpayloadType\x18\x01 \x01(\x0e\x32\x13.ProtoOAPayloadType:\x1dPROTO_OA_SYMBOL_CHANGED_EVENT\x12\x1b\n\x13\x63tidTraderAccountId\x18\x02 \x02(\x03\x12\x10\n\x08symbolId\x18\x03 \x03(\x03\"\x80\x01\n\x18ProtoOAAssetClassListReq\x12G\n\x0bpayloadType\x18\x01 \x01(\x0e\x32\x13.ProtoOAPayloadType:\x1dPROTO_OA_ASSET_CLASS_LIST_REQ\x12\x1b\n\x13\x63tidTraderAccountId\x18\x02 \x02(\x03\"\xa8\x01\n\x18ProtoOAAssetClassListRes\x12G\n\x0bpayloadType\x18\x01 \x01(\x0e\x32\x13.ProtoOAPayloadType:\x1dPROTO_OA_ASSET_CLASS_LIST_RES\x12\x1b\n\x13\x63tidTraderAccountId\x18\x02 \x02(\x03\x12&\n\nassetClass\x18\x03 \x03(\x0b\x32\x12.ProtoOAAssetClass\"n\n\x10ProtoOATraderReq\x12=\n\x0bpayloadType\x18\x01 \x01(\x0e\x32\x13.ProtoOAPayloadType:\x13PROTO_OA_TRADER_REQ\x12\x1b\n\x13\x63tidTraderAccountId\x18\x02 \x02(\x03\"\x8e\x01\n\x10ProtoOATraderRes\x12=\n\x0bpayloadType\x18\x01 \x01(\x0e\x32\x13.ProtoOAPayloadType:\x13PROTO_OA_TRADER_RES\x12\x1b\n\x13\x63tidTraderAccountId\x18\x02 \x02(\x03\x12\x1e\n\x06trader\x18\x03 \x02(\x0b\x32\x0e.ProtoOATrader\"\xa0\x01\n\x19ProtoOATraderUpdatedEvent\x12\x46\n\x0bpayloadType\x18\x01 \x01(\x0e\x32\x13.ProtoOAPayloadType:\x1cPROTO_OA_TRADER_UPDATE_EVENT\x12\x1b\n\x13\x63tidTraderAccountId\x18\x02 \x02(\x03\x12\x1e\n\x06trader\x18\x03 \x02(\x0b\x32\x0e.ProtoOATrader\"t\n\x13ProtoOAReconcileReq\x12@\n\x0bpayloadType\x18\x01 \x01(\x0e\x32\x13.ProtoOAPayloadType:\x16PROTO_OA_RECONCILE_REQ\x12\x1b\n\x13\x63tidTraderAccountId\x18\x02 \x02(\x03\"\xb6\x01\n\x13ProtoOAReconcileRes\x12@\n\x0bpayloadType\x18\x01 \x01(\x0e\x32\x13.ProtoOAPayloadType:\x16PROTO_OA_RECONCILE_RES\x12\x1b\n\x13\x63tidTraderAccountId\x18\x02 \x02(\x03\x12\"\n\x08position\x18\x03 \x03(\x0b\x32\x10.ProtoOAPosition\x12\x1c\n\x05order\x18\x04 \x03(\x0b\x32\r.ProtoOAOrder\"\xc8\x01\n\x16ProtoOAOrderErrorEvent\x12\x44\n\x0bpayloadType\x18\x01 \x01(\x0e\x32\x13.ProtoOAPayloadType:\x1aPROTO_OA_ORDER_ERROR_EVENT\x12\x1b\n\x13\x63tidTraderAccountId\x18\x05 \x02(\x03\x12\x11\n\terrorCode\x18\x02 \x02(\t\x12\x0f\n\x07orderId\x18\x03 \x01(\x03\x12\x12\n\npositionId\x18\x06 \x01(\x03\x12\x13\n\x0b\x64\x65scription\x18\x07 \x01(\t\"\xb0\x01\n\x12ProtoOADealListReq\x12@\n\x0bpayloadType\x18\x01 \x01(\x0e\x32\x13.ProtoOAPayloadType:\x16PROTO_OA_DEAL_LIST_REQ\x12\x1b\n\x13\x63tidTraderAccountId\x18\x02 \x02(\x03\x12\x15\n\rfromTimestamp\x18\x03 \x02(\x03\x12\x13\n\x0btoTimestamp\x18\x04 \x02(\x03\x12\x0f\n\x07maxRows\x18\x05 \x01(\x05\"\xa0\x01\n\x12ProtoOADealListRes\x12@\n\x0bpayloadType\x18\x01 \x01(\x0e\x32\x13.ProtoOAPayloadType:\x16PROTO_OA_DEAL_LIST_RES\x12\x1b\n\x13\x63tidTraderAccountId\x18\x02 \x02(\x03\x12\x1a\n\x04\x64\x65\x61l\x18\x03 \x03(\x0b\x32\x0c.ProtoOADeal\x12\x0f\n\x07hasMore\x18\x04 \x02(\x08\"\xa1\x01\n\x13ProtoOAOrderListReq\x12\x41\n\x0bpayloadType\x18\x01 \x01(\x0e\x32\x13.ProtoOAPayloadType:\x17PROTO_OA_ORDER_LIST_REQ\x12\x1b\n\x13\x63tidTraderAccountId\x18\x02 \x02(\x03\x12\x15\n\rfromTimestamp\x18\x03 \x02(\x03\x12\x13\n\x0btoTimestamp\x18\x04 \x02(\x03\"\xa4\x01\n\x13ProtoOAOrderListRes\x12\x41\n\x0bpayloadType\x18\x01 \x01(\x0e\x32\x13.ProtoOAPayloadType:\x17PROTO_OA_ORDER_LIST_RES\x12\x1b\n\x13\x63tidTraderAccountId\x18\x02 \x02(\x03\x12\x1c\n\x05order\x18\x03 \x03(\x0b\x32\r.ProtoOAOrder\x12\x0f\n\x07hasMore\x18\x04 \x02(\x08\"\xa1\x01\n\x18ProtoOAExpectedMarginReq\x12\x46\n\x0bpayloadType\x18\x01 \x01(\x0e\x32\x13.ProtoOAPayloadType:\x1cPROTO_OA_EXPECTED_MARGIN_REQ\x12\x1b\n\x13\x63tidTraderAccountId\x18\x02 \x02(\x03\x12\x10\n\x08symbolId\x18\x03 \x02(\x03\x12\x0e\n\x06volume\x18\x04 \x03(\x03\"\xbc\x01\n\x18ProtoOAExpectedMarginRes\x12\x46\n\x0bpayloadType\x18\x01 \x01(\x0e\x32\x13.ProtoOAPayloadType:\x1cPROTO_OA_EXPECTED_MARGIN_RES\x12\x1b\n\x13\x63tidTraderAccountId\x18\x02 \x02(\x03\x12&\n\x06margin\x18\x03 \x03(\x0b\x32\x16.ProtoOAExpectedMargin\x12\x13\n\x0bmoneyDigits\x18\x04 \x01(\r\"\xbe\x01\n\x19ProtoOAMarginChangedEvent\x12G\n\x0bpayloadType\x18\x01 \x01(\x0e\x32\x13.ProtoOAPayloadType:\x1dPROTO_OA_MARGIN_CHANGED_EVENT\x12\x1b\n\x13\x63tidTraderAccountId\x18\x02 \x02(\x03\x12\x12\n\npositionId\x18\x03 \x02(\x04\x12\x12\n\nusedMargin\x18\x04 \x02(\x04\x12\x13\n\x0bmoneyDigits\x18\x05 \x01(\r\"\xb7\x01\n\x1dProtoOACashFlowHistoryListReq\x12M\n\x0bpayloadType\x18\x01 \x01(\x0e\x32\x13.ProtoOAPayloadType:#PROTO_OA_CASH_FLOW_HISTORY_LIST_REQ\x12\x1b\n\x13\x63tidTraderAccountId\x18\x02 \x02(\x03\x12\x15\n\rfromTimestamp\x18\x03 \x02(\x03\x12\x13\n\x0btoTimestamp\x18\x04 \x02(\x03\"\xbd\x01\n\x1dProtoOACashFlowHistoryListRes\x12M\n\x0bpayloadType\x18\x01 \x01(\x0e\x32\x13.ProtoOAPayloadType:#PROTO_OA_CASH_FLOW_HISTORY_LIST_RES\x12\x1b\n\x13\x63tidTraderAccountId\x18\x02 \x02(\x03\x12\x30\n\x0f\x64\x65positWithdraw\x18\x03 \x03(\x0b\x32\x17.ProtoOADepositWithdraw\"\x91\x01\n%ProtoOAGetAccountListByAccessTokenReq\x12S\n\x0bpayloadType\x18\x01 \x01(\x0e\x32\x13.ProtoOAPayloadType:)PROTO_OA_GET_ACCOUNTS_BY_ACCESS_TOKEN_REQ\x12\x13\n\x0b\x61\x63\x63\x65ssToken\x18\x02 \x02(\t\"\xff\x01\n%ProtoOAGetAccountListByAccessTokenRes\x12S\n\x0bpayloadType\x18\x01 \x01(\x0e\x32\x13.ProtoOAPayloadType:)PROTO_OA_GET_ACCOUNTS_BY_ACCESS_TOKEN_RES\x12\x13\n\x0b\x61\x63\x63\x65ssToken\x18\x02 \x02(\t\x12\x36\n\x0fpermissionScope\x18\x03 \x01(\x0e\x32\x1d.ProtoOAClientPermissionScope\x12\x34\n\x11\x63tidTraderAccount\x18\x04 \x03(\x0b\x32\x19.ProtoOACtidTraderAccount\"t\n\x16ProtoOARefreshTokenReq\x12\x44\n\x0bpayloadType\x18\x01 \x01(\x0e\x32\x13.ProtoOAPayloadType:\x1aPROTO_OA_REFRESH_TOKEN_REQ\x12\x14\n\x0crefreshToken\x18\x02 \x02(\t\"\xaf\x01\n\x16ProtoOARefreshTokenRes\x12\x44\n\x0bpayloadType\x18\x01 \x01(\x0e\x32\x13.ProtoOAPayloadType:\x1aPROTO_OA_REFRESH_TOKEN_RES\x12\x13\n\x0b\x61\x63\x63\x65ssToken\x18\x02 \x02(\t\x12\x11\n\ttokenType\x18\x03 \x02(\t\x12\x11\n\texpiresIn\x18\x04 \x02(\x03\x12\x14\n\x0crefreshToken\x18\x05 \x02(\t\"\xb3\x01\n\x18ProtoOASubscribeSpotsReq\x12\x46\n\x0bpayloadType\x18\x01 \x01(\x0e\x32\x13.ProtoOAPayloadType:\x1cPROTO_OA_SUBSCRIBE_SPOTS_REQ\x12\x1b\n\x13\x63tidTraderAccountId\x18\x02 \x02(\x03\x12\x10\n\x08symbolId\x18\x03 \x03(\x03\x12 \n\x18subscribeToSpotTimestamp\x18\x04 \x01(\x08\"\x7f\n\x18ProtoOASubscribeSpotsRes\x12\x46\n\x0bpayloadType\x18\x01 \x01(\x0e\x32\x13.ProtoOAPayloadType:\x1cPROTO_OA_SUBSCRIBE_SPOTS_RES\x12\x1b\n\x13\x63tidTraderAccountId\x18\x02 \x02(\x03\"\x95\x01\n\x1aProtoOAUnsubscribeSpotsReq\x12H\n\x0bpayloadType\x18\x01 \x01(\x0e\x32\x13.ProtoOAPayloadType:\x1ePROTO_OA_UNSUBSCRIBE_SPOTS_REQ\x12\x1b\n\x13\x63tidTraderAccountId\x18\x02 \x02(\x03\x12\x10\n\x08symbolId\x18\x03 \x03(\x03\"\x83\x01\n\x1aProtoOAUnsubscribeSpotsRes\x12H\n\x0bpayloadType\x18\x01 \x01(\x0e\x32\x13.ProtoOAPayloadType:\x1ePROTO_OA_UNSUBSCRIBE_SPOTS_RES\x12\x1b\n\x13\x63tidTraderAccountId\x18\x02 \x02(\x03\"\xe7\x01\n\x10ProtoOASpotEvent\x12=\n\x0bpayloadType\x18\x01 \x01(\x0e\x32\x13.ProtoOAPayloadType:\x13PROTO_OA_SPOT_EVENT\x12\x1b\n\x13\x63tidTraderAccountId\x18\x02 \x02(\x03\x12\x10\n\x08symbolId\x18\x03 \x02(\x03\x12\x0b\n\x03\x62id\x18\x04 \x01(\x04\x12\x0b\n\x03\x61sk\x18\x05 \x01(\x04\x12\"\n\x08trendbar\x18\x06 \x03(\x0b\x32\x10.ProtoOATrendbar\x12\x14\n\x0csessionClose\x18\x07 \x01(\x04\x12\x11\n\ttimestamp\x18\x08 \x01(\x03\"\xc8\x01\n\x1fProtoOASubscribeLiveTrendbarReq\x12N\n\x0bpayloadType\x18\x01 \x01(\x0e\x32\x13.ProtoOAPayloadType:$PROTO_OA_SUBSCRIBE_LIVE_TRENDBAR_REQ\x12\x1b\n\x13\x63tidTraderAccountId\x18\x02 \x02(\x03\x12&\n\x06period\x18\x03 \x02(\x0e\x32\x16.ProtoOATrendbarPeriod\x12\x10\n\x08symbolId\x18\x04 \x02(\x03\"\x8e\x01\n\x1fProtoOASubscribeLiveTrendbarRes\x12N\n\x0bpayloadType\x18\x01 \x01(\x0e\x32\x13.ProtoOAPayloadType:$PROTO_OA_SUBSCRIBE_LIVE_TRENDBAR_RES\x12\x1b\n\x13\x63tidTraderAccountId\x18\x02 \x02(\x03\"\xcc\x01\n!ProtoOAUnsubscribeLiveTrendbarReq\x12P\n\x0bpayloadType\x18\x01 \x01(\x0e\x32\x13.ProtoOAPayloadType:&PROTO_OA_UNSUBSCRIBE_LIVE_TRENDBAR_REQ\x12\x1b\n\x13\x63tidTraderAccountId\x18\x02 \x02(\x03\x12&\n\x06period\x18\x03 \x02(\x0e\x32\x16.ProtoOATrendbarPeriod\x12\x10\n\x08symbolId\x18\x04 \x02(\x03\"\x92\x01\n!ProtoOAUnsubscribeLiveTrendbarRes\x12P\n\x0bpayloadType\x18\x01 \x01(\x0e\x32\x13.ProtoOAPayloadType:&PROTO_OA_UNSUBSCRIBE_LIVE_TRENDBAR_RES\x12\x1b\n\x13\x63tidTraderAccountId\x18\x02 \x02(\x03\"\xf0\x01\n\x16ProtoOAGetTrendbarsReq\x12\x44\n\x0bpayloadType\x18\x01 \x01(\x0e\x32\x13.ProtoOAPayloadType:\x1aPROTO_OA_GET_TRENDBARS_REQ\x12\x1b\n\x13\x63tidTraderAccountId\x18\x02 \x02(\x03\x12\x15\n\rfromTimestamp\x18\x03 \x02(\x03\x12\x13\n\x0btoTimestamp\x18\x04 \x02(\x03\x12&\n\x06period\x18\x05 \x02(\x0e\x32\x16.ProtoOATrendbarPeriod\x12\x10\n\x08symbolId\x18\x06 \x02(\x03\x12\r\n\x05\x63ount\x18\x07 \x01(\r\"\xec\x01\n\x16ProtoOAGetTrendbarsRes\x12\x44\n\x0bpayloadType\x18\x01 \x01(\x0e\x32\x13.ProtoOAPayloadType:\x1aPROTO_OA_GET_TRENDBARS_RES\x12\x1b\n\x13\x63tidTraderAccountId\x18\x02 \x02(\x03\x12&\n\x06period\x18\x03 \x02(\x0e\x32\x16.ProtoOATrendbarPeriod\x12\x11\n\ttimestamp\x18\x04 \x02(\x03\x12\"\n\x08trendbar\x18\x05 \x03(\x0b\x32\x10.ProtoOATrendbar\x12\x10\n\x08symbolId\x18\x06 \x01(\x03\"\xd8\x01\n\x15ProtoOAGetTickDataReq\x12\x43\n\x0bpayloadType\x18\x01 \x01(\x0e\x32\x13.ProtoOAPayloadType:\x19PROTO_OA_GET_TICKDATA_REQ\x12\x1b\n\x13\x63tidTraderAccountId\x18\x02 \x02(\x03\x12\x10\n\x08symbolId\x18\x03 \x02(\x03\x12\x1f\n\x04type\x18\x04 \x02(\x0e\x32\x11.ProtoOAQuoteType\x12\x15\n\rfromTimestamp\x18\x05 \x02(\x03\x12\x13\n\x0btoTimestamp\x18\x06 \x02(\x03\"\xae\x01\n\x15ProtoOAGetTickDataRes\x12\x43\n\x0bpayloadType\x18\x01 \x01(\x0e\x32\x13.ProtoOAPayloadType:\x19PROTO_OA_GET_TICKDATA_RES\x12\x1b\n\x13\x63tidTraderAccountId\x18\x02 \x02(\x03\x12\"\n\x08tickData\x18\x03 \x03(\x0b\x32\x10.ProtoOATickData\x12\x0f\n\x07hasMore\x18\x04 \x02(\x08\"\x88\x01\n\x1fProtoOAGetCtidProfileByTokenReq\x12P\n\x0bpayloadType\x18\x01 \x01(\x0e\x32\x13.ProtoOAPayloadType:&PROTO_OA_GET_CTID_PROFILE_BY_TOKEN_REQ\x12\x13\n\x0b\x61\x63\x63\x65ssToken\x18\x02 \x02(\t\"\x99\x01\n\x1fProtoOAGetCtidProfileByTokenRes\x12P\n\x0bpayloadType\x18\x01 \x01(\x0e\x32\x13.ProtoOAPayloadType:&PROTO_OA_GET_CTID_PROFILE_BY_TOKEN_RES\x12$\n\x07profile\x18\x02 \x02(\x0b\x32\x13.ProtoOACtidProfile\"\xc4\x01\n\x11ProtoOADepthEvent\x12>\n\x0bpayloadType\x18\x01 \x01(\x0e\x32\x13.ProtoOAPayloadType:\x14PROTO_OA_DEPTH_EVENT\x12\x1b\n\x13\x63tidTraderAccountId\x18\x02 \x02(\x03\x12\x10\n\x08symbolId\x18\x03 \x02(\x04\x12%\n\tnewQuotes\x18\x04 \x03(\x0b\x32\x12.ProtoOADepthQuote\x12\x19\n\rdeletedQuotes\x18\x05 \x03(\x04\x42\x02\x10\x01\"\x9e\x01\n\x1eProtoOASubscribeDepthQuotesReq\x12M\n\x0bpayloadType\x18\x01 \x01(\x0e\x32\x13.ProtoOAPayloadType:#PROTO_OA_SUBSCRIBE_DEPTH_QUOTES_REQ\x12\x1b\n\x13\x63tidTraderAccountId\x18\x02 \x02(\x03\x12\x10\n\x08symbolId\x18\x03 \x03(\x03\"\x8c\x01\n\x1eProtoOASubscribeDepthQuotesRes\x12M\n\x0bpayloadType\x18\x01 \x01(\x0e\x32\x13.ProtoOAPayloadType:#PROTO_OA_SUBSCRIBE_DEPTH_QUOTES_RES\x12\x1b\n\x13\x63tidTraderAccountId\x18\x02 \x02(\x03\"\xa2\x01\n ProtoOAUnsubscribeDepthQuotesReq\x12O\n\x0bpayloadType\x18\x01 \x01(\x0e\x32\x13.ProtoOAPayloadType:%PROTO_OA_UNSUBSCRIBE_DEPTH_QUOTES_REQ\x12\x1b\n\x13\x63tidTraderAccountId\x18\x02 \x02(\x03\x12\x10\n\x08symbolId\x18\x03 \x03(\x03\"\x90\x01\n ProtoOAUnsubscribeDepthQuotesRes\x12O\n\x0bpayloadType\x18\x01 \x01(\x0e\x32\x13.ProtoOAPayloadType:%PROTO_OA_UNSUBSCRIBE_DEPTH_QUOTES_RES\x12\x1b\n\x13\x63tidTraderAccountId\x18\x02 \x02(\x03\"\x83\x01\n\x1cProtoOASymbolCategoryListReq\x12\x46\n\x0bpayloadType\x18\x01 \x01(\x0e\x32\x13.ProtoOAPayloadType:\x1cPROTO_OA_SYMBOL_CATEGORY_REQ\x12\x1b\n\x13\x63tidTraderAccountId\x18\x02 \x02(\x03\"\xb3\x01\n\x1cProtoOASymbolCategoryListRes\x12\x46\n\x0bpayloadType\x18\x01 \x01(\x0e\x32\x13.ProtoOAPayloadType:\x1cPROTO_OA_SYMBOL_CATEGORY_RES\x12\x1b\n\x13\x63tidTraderAccountId\x18\x02 \x02(\x03\x12.\n\x0esymbolCategory\x18\x03 \x03(\x0b\x32\x16.ProtoOASymbolCategory\"}\n\x17ProtoOAAccountLogoutReq\x12\x45\n\x0bpayloadType\x18\x01 \x01(\x0e\x32\x13.ProtoOAPayloadType:\x1bPROTO_OA_ACCOUNT_LOGOUT_REQ\x12\x1b\n\x13\x63tidTraderAccountId\x18\x02 \x02(\x03\"}\n\x17ProtoOAAccountLogoutRes\x12\x45\n\x0bpayloadType\x18\x01 \x01(\x0e\x32\x13.ProtoOAPayloadType:\x1bPROTO_OA_ACCOUNT_LOGOUT_RES\x12\x1b\n\x13\x63tidTraderAccountId\x18\x02 \x02(\x03\"\x89\x01\n\x1dProtoOAAccountDisconnectEvent\x12K\n\x0bpayloadType\x18\x01 \x01(\x0e\x32\x13.ProtoOAPayloadType:!PROTO_OA_ACCOUNT_DISCONNECT_EVENT\x12\x1b\n\x13\x63tidTraderAccountId\x18\x02 \x02(\x03\"\x80\x01\n\x18ProtoOAMarginCallListReq\x12G\n\x0bpayloadType\x18\x01 \x01(\x0e\x32\x13.ProtoOAPayloadType:\x1dPROTO_OA_MARGIN_CALL_LIST_REQ\x12\x1b\n\x13\x63tidTraderAccountId\x18\x02 \x02(\x03\"\x8b\x01\n\x18ProtoOAMarginCallListRes\x12G\n\x0bpayloadType\x18\x01 \x01(\x0e\x32\x13.ProtoOAPayloadType:\x1dPROTO_OA_MARGIN_CALL_LIST_RES\x12&\n\nmarginCall\x18\x02 \x03(\x0b\x32\x12.ProtoOAMarginCall\"\xac\x01\n\x1aProtoOAMarginCallUpdateReq\x12I\n\x0bpayloadType\x18\x01 \x01(\x0e\x32\x13.ProtoOAPayloadType:\x1fPROTO_OA_MARGIN_CALL_UPDATE_REQ\x12\x1b\n\x13\x63tidTraderAccountId\x18\x02 \x02(\x03\x12&\n\nmarginCall\x18\x03 \x02(\x0b\x32\x12.ProtoOAMarginCall\"g\n\x1aProtoOAMarginCallUpdateRes\x12I\n\x0bpayloadType\x18\x01 \x01(\x0e\x32\x13.ProtoOAPayloadType:\x1fPROTO_OA_MARGIN_CALL_UPDATE_RES\"\xb0\x01\n\x1cProtoOAMarginCallUpdateEvent\x12K\n\x0bpayloadType\x18\x01 \x01(\x0e\x32\x13.ProtoOAPayloadType:!PROTO_OA_MARGIN_CALL_UPDATE_EVENT\x12\x1b\n\x13\x63tidTraderAccountId\x18\x02 \x02(\x03\x12&\n\nmarginCall\x18\x03 \x02(\x0b\x32\x12.ProtoOAMarginCall\"\xb2\x01\n\x1dProtoOAMarginCallTriggerEvent\x12L\n\x0bpayloadType\x18\x01 \x01(\x0e\x32\x13.ProtoOAPayloadType:\"PROTO_OA_MARGIN_CALL_TRIGGER_EVENT\x12\x1b\n\x13\x63tidTraderAccountId\x18\x02 \x02(\x03\x12&\n\nmarginCall\x18\x03 \x02(\x0b\x32\x12.ProtoOAMarginCall\"\xa0\x01\n ProtoOAGetDynamicLeverageByIDReq\x12K\n\x0bpayloadType\x18\x01 \x01(\x0e\x32\x13.ProtoOAPayloadType:!PROTO_OA_GET_DYNAMIC_LEVERAGE_REQ\x12\x1b\n\x13\x63tidTraderAccountId\x18\x02 \x02(\x03\x12\x12\n\nleverageId\x18\x03 \x02(\x03\"\xb7\x01\n ProtoOAGetDynamicLeverageByIDRes\x12K\n\x0bpayloadType\x18\x01 \x01(\x0e\x32\x13.ProtoOAPayloadType:!PROTO_OA_GET_DYNAMIC_LEVERAGE_RES\x12\x1b\n\x13\x63tidTraderAccountId\x18\x02 \x02(\x03\x12)\n\x08leverage\x18\x03 \x02(\x0b\x32\x17.ProtoOADynamicLeverage\"\xce\x01\n\x1eProtoOADealListByPositionIdReq\x12O\n\x0bpayloadType\x18\x01 \x01(\x0e\x32\x13.ProtoOAPayloadType:%PROTO_OA_DEAL_LIST_BY_POSITION_ID_REQ\x12\x1b\n\x13\x63tidTraderAccountId\x18\x02 \x02(\x03\x12\x12\n\npositionId\x18\x03 \x02(\x03\x12\x15\n\rfromTimestamp\x18\x04 \x02(\x03\x12\x13\n\x0btoTimestamp\x18\x05 \x02(\x03\"\xbb\x01\n\x1eProtoOADealListByPositionIdRes\x12O\n\x0bpayloadType\x18\x01 \x01(\x0e\x32\x13.ProtoOAPayloadType:%PROTO_OA_DEAL_LIST_BY_POSITION_ID_RES\x12\x1b\n\x13\x63tidTraderAccountId\x18\x02 \x02(\x03\x12\x1a\n\x04\x64\x65\x61l\x18\x03 \x03(\x0b\x32\x0c.ProtoOADeal\x12\x0f\n\x07hasMore\x18\x04 \x01(\x03\"\x90\x01\n\x18ProtoOADealOffsetListReq\x12G\n\x0bpayloadType\x18\x01 \x01(\x0e\x32\x13.ProtoOAPayloadType:\x1dPROTO_OA_DEAL_OFFSET_LIST_REQ\x12\x1b\n\x13\x63tidTraderAccountId\x18\x02 \x02(\x03\x12\x0e\n\x06\x64\x65\x61lId\x18\x03 \x02(\x03\"\xce\x01\n\x18ProtoOADealOffsetListRes\x12G\n\x0bpayloadType\x18\x01 \x01(\x0e\x32\x13.ProtoOAPayloadType:\x1dPROTO_OA_DEAL_OFFSET_LIST_RES\x12\x1b\n\x13\x63tidTraderAccountId\x18\x02 \x02(\x03\x12$\n\x08offsetBy\x18\x03 \x03(\x0b\x32\x12.ProtoOADealOffset\x12&\n\noffsetting\x18\x04 \x03(\x0b\x32\x12.ProtoOADealOffset\"\x95\x01\n\"ProtoOAGetPositionUnrealizedPnLReq\x12R\n\x0bpayloadType\x18\x01 \x01(\x0e\x32\x13.ProtoOAPayloadType:(PROTO_OA_GET_POSITION_UNREALIZED_PNL_REQ\x12\x1b\n\x13\x63tidTraderAccountId\x18\x02 \x02(\x03\"\xe8\x01\n\"ProtoOAGetPositionUnrealizedPnLRes\x12R\n\x0bpayloadType\x18\x01 \x01(\x0e\x32\x13.ProtoOAPayloadType:(PROTO_OA_GET_POSITION_UNREALIZED_PNL_RES\x12\x1b\n\x13\x63tidTraderAccountId\x18\x02 \x02(\x03\x12<\n\x15positionUnrealizedPnL\x18\x03 \x03(\x0b\x32\x1d.ProtoOAPositionUnrealizedPnL\x12\x13\n\x0bmoneyDigits\x18\x04 \x02(\r\"\x8c\x01\n\x16ProtoOAOrderDetailsReq\x12\x44\n\x0bpayloadType\x18\x01 \x01(\x0e\x32\x13.ProtoOAPayloadType:\x1aPROTO_OA_ORDER_DETAILS_REQ\x12\x1b\n\x13\x63tidTraderAccountId\x18\x02 \x02(\x03\x12\x0f\n\x07orderId\x18\x03 \x02(\x03\"\xb5\x01\n\x16ProtoOAOrderDetailsRes\x12\x44\n\x0bpayloadType\x18\x01 \x01(\x0e\x32\x13.ProtoOAPayloadType:\x1aPROTO_OA_ORDER_DETAILS_RES\x12\x1b\n\x13\x63tidTraderAccountId\x18\x02 \x02(\x03\x12\x1c\n\x05order\x18\x03 \x02(\x0b\x32\r.ProtoOAOrder\x12\x1a\n\x04\x64\x65\x61l\x18\x04 \x03(\x0b\x32\x0c.ProtoOADeal\"\xd0\x01\n\x1fProtoOAOrderListByPositionIdReq\x12P\n\x0bpayloadType\x18\x01 \x01(\x0e\x32\x13.ProtoOAPayloadType:&PROTO_OA_ORDER_LIST_BY_POSITION_ID_REQ\x12\x1b\n\x13\x63tidTraderAccountId\x18\x02 \x02(\x03\x12\x12\n\npositionId\x18\x03 \x02(\x03\x12\x15\n\rfromTimestamp\x18\x04 \x01(\x03\x12\x13\n\x0btoTimestamp\x18\x05 \x01(\x03\"\xbf\x01\n\x1fProtoOAOrderListByPositionIdRes\x12P\n\x0bpayloadType\x18\x01 \x01(\x0e\x32\x13.ProtoOAPayloadType:&PROTO_OA_ORDER_LIST_BY_POSITION_ID_RES\x12\x1b\n\x13\x63tidTraderAccountId\x18\x02 \x02(\x03\x12\x1c\n\x05order\x18\x03 \x03(\x0b\x32\r.ProtoOAOrder\x12\x0f\n\x07hasMore\x18\x04 \x01(\x03\"\xc9\x01\n\x17ProtoOAv1PnLChangeEvent\x12\x46\n\x0bpayloadType\x18\x01 \x01(\x0e\x32\x13.ProtoOAPayloadType:\x1cPROTO_OA_V1_PNL_CHANGE_EVENT\x12\x1b\n\x13\x63tidTraderAccountId\x18\x02 \x02(\x03\x12\x1a\n\x12grossUnrealizedPnL\x18\x03 \x02(\x03\x12\x18\n\x10netUnrealizedPnL\x18\x04 \x02(\x03\x12\x13\n\x0bmoneyDigits\x18\x05 \x02(\r\"\x8d\x01\n\x1eProtoOAv1PnLChangeSubscribeReq\x12N\n\x0bpayloadType\x18\x01 \x01(\x0e\x32\x13.ProtoOAPayloadType:$PROTO_OA_V1_PNL_CHANGE_SUBSCRIBE_REQ\x12\x1b\n\x13\x63tidTraderAccountId\x18\x02 \x02(\x03\"\x8d\x01\n\x1eProtoOAv1PnLChangeSubscribeRes\x12N\n\x0bpayloadType\x18\x01 \x01(\x0e\x32\x13.ProtoOAPayloadType:$PROTO_OA_V1_PNL_CHANGE_SUBSCRIBE_RES\x12\x1b\n\x13\x63tidTraderAccountId\x18\x02 \x02(\x03\"\x92\x01\n ProtoOAv1PnLChangeUnSubscribeReq\x12Q\n\x0bpayloadType\x18\x01 \x01(\x0e\x32\x13.ProtoOAPayloadType:\'PROTO_OA_V1_PNL_CHANGE_UN_SUBSCRIBE_REQ\x12\x1b\n\x13\x63tidTraderAccountId\x18\x02 \x02(\x03\"\x92\x01\n ProtoOAv1PnLChangeUnSubscribeRes\x12Q\n\x0bpayloadType\x18\x01 \x01(\x0e\x32\x13.ProtoOAPayloadType:\'PROTO_OA_V1_PNL_CHANGE_UN_SUBSCRIBE_RES\x12\x1b\n\x13\x63tidTraderAccountId\x18\x02 \x02(\x08\x42\x42\n\x1f\x63om.xtrader.protocol.openapi.v2B\x1a\x43ontainerOpenApiV2MessagesP\x01\xa0\x01\x01')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'OpenApiMessages_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\037com.xtrader.protocol.openapi.v2B\032ContainerOpenApiV2MessagesP\001\240\001\001'
  _PROTOOADEPTHEVENT.fields_by_name['deletedQuotes']._options = None
  _PROTOOADEPTHEVENT.fields_by_name['deletedQuotes']._serialized_options = b'\020\001'
  _PROTOOAAPPLICATIONAUTHREQ._serialized_start=54
  _PROTOOAAPPLICATIONAUTHREQ._serialized_end=194
  _PROTOOAAPPLICATIONAUTHRES._serialized_start=196
  _PROTOOAAPPLICATIONAUTHRES._serialized_end=296
  _PROTOOAACCOUNTAUTHREQ._serialized_start=299
  _PROTOOAACCOUNTAUTHREQ._serialized_end=441
  _PROTOOAACCOUNTAUTHRES._serialized_start=443
  _PROTOOAACCOUNTAUTHRES._serialized_end=564
  _PROTOOAERRORRES._serialized_start=567
  _PROTOOAERRORRES._serialized_end=748
  _PROTOOACLIENTDISCONNECTEVENT._serialized_start=750
  _PROTOOACLIENTDISCONNECTEVENT._serialized_end=872
  _PROTOOAACCOUNTSTOKENINVALIDATEDEVENT._serialized_start=875
  _PROTOOAACCOUNTSTOKENINVALIDATEDEVENT._serialized_end=1044
  _PROTOOAVERSIONREQ._serialized_start=1046
  _PROTOOAVERSIONREQ._serialized_end=1129
  _PROTOOAVERSIONRES._serialized_start=1131
  _PROTOOAVERSIONRES._serialized_end=1231
  _PROTOOANEWORDERREQ._serialized_start=1234
  _PROTOOANEWORDERREQ._serialized_end=1923
  _PROTOOAEXECUTIONEVENT._serialized_start=1926
  _PROTOOAEXECUTIONEVENT._serialized_end=2338
  _PROTOOACANCELORDERREQ._serialized_start=2341
  _PROTOOACANCELORDERREQ._serialized_end=2479
  _PROTOOAAMENDORDERREQ._serialized_start=2482
  _PROTOOAAMENDORDERREQ._serialized_end=2936
  _PROTOOAAMENDPOSITIONSLTPREQ._serialized_start=2939
  _PROTOOAAMENDPOSITIONSLTPREQ._serialized_end=3251
  _PROTOOACLOSEPOSITIONREQ._serialized_start=3254
  _PROTOOACLOSEPOSITIONREQ._serialized_end=3415
  _PROTOOATRAILINGSLCHANGEDEVENT._serialized_start=3418
  _PROTOOATRAILINGSLCHANGEDEVENT._serialized_end=3644
  _PROTOOAASSETLISTREQ._serialized_start=3646
  _PROTOOAASSETLISTREQ._serialized_end=3763
  _PROTOOAASSETLISTRES._serialized_start=3766
  _PROTOOAASSETLISTRES._serialized_end=3913
  _PROTOOASYMBOLSLISTREQ._serialized_start=3916
  _PROTOOASYMBOLSLISTREQ._serialized_end=4076
  _PROTOOASYMBOLSLISTRES._serialized_start=4079
  _PROTOOASYMBOLSLISTRES._serialized_end=4285
  _PROTOOASYMBOLBYIDREQ._serialized_start=4288
  _PROTOOASYMBOLBYIDREQ._serialized_end=4426
  _PROTOOASYMBOLBYIDRES._serialized_start=4429
  _PROTOOASYMBOLBYIDRES._serialized_end=4629
  _PROTOOASYMBOLSFORCONVERSIONREQ._serialized_start=4632
  _PROTOOASYMBOLSFORCONVERSIONREQ._serialized_end=4815
  _PROTOOASYMBOLSFORCONVERSIONRES._serialized_start=4818
  _PROTOOASYMBOLSFORCONVERSIONRES._serialized_end=4995
  _PROTOOASYMBOLCHANGEDEVENT._serialized_start=4998
  _PROTOOASYMBOLCHANGEDEVENT._serialized_end=5145
  _PROTOOAASSETCLASSLISTREQ._serialized_start=5148
  _PROTOOAASSETCLASSLISTREQ._serialized_end=5276
  _PROTOOAASSETCLASSLISTRES._serialized_start=5279
  _PROTOOAASSETCLASSLISTRES._serialized_end=5447
  _PROTOOATRADERREQ._serialized_start=5449
  _PROTOOATRADERREQ._serialized_end=5559
  _PROTOOATRADERRES._serialized_start=5562
  _PROTOOATRADERRES._serialized_end=5704
  _PROTOOATRADERUPDATEDEVENT._serialized_start=5707
  _PROTOOATRADERUPDATEDEVENT._serialized_end=5867
  _PROTOOARECONCILEREQ._serialized_start=5869
  _PROTOOARECONCILEREQ._serialized_end=5985
  _PROTOOARECONCILERES._serialized_start=5988
  _PROTOOARECONCILERES._serialized_end=6170
  _PROTOOAORDERERROREVENT._serialized_start=6173
  _PROTOOAORDERERROREVENT._serialized_end=6373
  _PROTOOADEALLISTREQ._serialized_start=6376
  _PROTOOADEALLISTREQ._serialized_end=6552
  _PROTOOADEALLISTRES._serialized_start=6555
  _PROTOOADEALLISTRES._serialized_end=6715
  _PROTOOAORDERLISTREQ._serialized_start=6718
  _PROTOOAORDERLISTREQ._serialized_end=6879
  _PROTOOAORDERLISTRES._serialized_start=6882
  _PROTOOAORDERLISTRES._serialized_end=7046
  _PROTOOAEXPECTEDMARGINREQ._serialized_start=7049
  _PROTOOAEXPECTEDMARGINREQ._serialized_end=7210
  _PROTOOAEXPECTEDMARGINRES._serialized_start=7213
  _PROTOOAEXPECTEDMARGINRES._serialized_end=7401
  _PROTOOAMARGINCHANGEDEVENT._serialized_start=7404
  _PROTOOAMARGINCHANGEDEVENT._serialized_end=7594
  _PROTOOACASHFLOWHISTORYLISTREQ._serialized_start=7597
  _PROTOOACASHFLOWHISTORYLISTREQ._serialized_end=7780
  _PROTOOACASHFLOWHISTORYLISTRES._serialized_start=7783
  _PROTOOACASHFLOWHISTORYLISTRES._serialized_end=7972
  _PROTOOAGETACCOUNTLISTBYACCESSTOKENREQ._serialized_start=7975
  _PROTOOAGETACCOUNTLISTBYACCESSTOKENREQ._serialized_end=8120
  _PROTOOAGETACCOUNTLISTBYACCESSTOKENRES._serialized_start=8123
  _PROTOOAGETACCOUNTLISTBYACCESSTOKENRES._serialized_end=8378
  _PROTOOAREFRESHTOKENREQ._serialized_start=8380
  _PROTOOAREFRESHTOKENREQ._serialized_end=8496
  _PROTOOAREFRESHTOKENRES._serialized_start=8499
  _PROTOOAREFRESHTOKENRES._serialized_end=8674
  _PROTOOASUBSCRIBESPOTSREQ._serialized_start=8677
  _PROTOOASUBSCRIBESPOTSREQ._serialized_end=8856
  _PROTOOASUBSCRIBESPOTSRES._serialized_start=8858
  _PROTOOASUBSCRIBESPOTSRES._serialized_end=8985
  _PROTOOAUNSUBSCRIBESPOTSREQ._serialized_start=8988
  _PROTOOAUNSUBSCRIBESPOTSREQ._serialized_end=9137
  _PROTOOAUNSUBSCRIBESPOTSRES._serialized_start=9140
  _PROTOOAUNSUBSCRIBESPOTSRES._serialized_end=9271
  _PROTOOASPOTEVENT._serialized_start=9274
  _PROTOOASPOTEVENT._serialized_end=9505
  _PROTOOASUBSCRIBELIVETRENDBARREQ._serialized_start=9508
  _PROTOOASUBSCRIBELIVETRENDBARREQ._serialized_end=9708
  _PROTOOASUBSCRIBELIVETRENDBARRES._serialized_start=9711
  _PROTOOASUBSCRIBELIVETRENDBARRES._serialized_end=9853
  _PROTOOAUNSUBSCRIBELIVETRENDBARREQ._serialized_start=9856
  _PROTOOAUNSUBSCRIBELIVETRENDBARREQ._serialized_end=10060
  _PROTOOAUNSUBSCRIBELIVETRENDBARRES._serialized_start=10063
  _PROTOOAUNSUBSCRIBELIVETRENDBARRES._serialized_end=10209
  _PROTOOAGETTRENDBARSREQ._serialized_start=10212
  _PROTOOAGETTRENDBARSREQ._serialized_end=10452
  _PROTOOAGETTRENDBARSRES._serialized_start=10455
  _PROTOOAGETTRENDBARSRES._serialized_end=10691
  _PROTOOAGETTICKDATAREQ._serialized_start=10694
  _PROTOOAGETTICKDATAREQ._serialized_end=10910
  _PROTOOAGETTICKDATARES._serialized_start=10913
  _PROTOOAGETTICKDATARES._serialized_end=11087
  _PROTOOAGETCTIDPROFILEBYTOKENREQ._serialized_start=11090
  _PROTOOAGETCTIDPROFILEBYTOKENREQ._serialized_end=11226
  _PROTOOAGETCTIDPROFILEBYTOKENRES._serialized_start=11229
  _PROTOOAGETCTIDPROFILEBYTOKENRES._serialized_end=11382
  _PROTOOADEPTHEVENT._serialized_start=11385
  _PROTOOADEPTHEVENT._serialized_end=11581
  _PROTOOASUBSCRIBEDEPTHQUOTESREQ._serialized_start=11584
  _PROTOOASUBSCRIBEDEPTHQUOTESREQ._serialized_end=11742
  _PROTOOASUBSCRIBEDEPTHQUOTESRES._serialized_start=11745
  _PROTOOASUBSCRIBEDEPTHQUOTESRES._serialized_end=11885
  _PROTOOAUNSUBSCRIBEDEPTHQUOTESREQ._serialized_start=11888
  _PROTOOAUNSUBSCRIBEDEPTHQUOTESREQ._serialized_end=12050
  _PROTOOAUNSUBSCRIBEDEPTHQUOTESRES._serialized_start=12053
  _PROTOOAUNSUBSCRIBEDEPTHQUOTESRES._serialized_end=12197
  _PROTOOASYMBOLCATEGORYLISTREQ._serialized_start=12200
  _PROTOOASYMBOLCATEGORYLISTREQ._serialized_end=12331
  _PROTOOASYMBOLCATEGORYLISTRES._serialized_start=12334
  _PROTOOASYMBOLCATEGORYLISTRES._serialized_end=12513
  _PROTOOAACCOUNTLOGOUTREQ._serialized_start=12515
  _PROTOOAACCOUNTLOGOUTREQ._serialized_end=12640
  _PROTOOAACCOUNTLOGOUTRES._serialized_start=12642
  _PROTOOAACCOUNTLOGOUTRES._serialized_end=12767
  _PROTOOAACCOUNTDISCONNECTEVENT._serialized_start=12770
  _PROTOOAACCOUNTDISCONNECTEVENT._serialized_end=12907
  _PROTOOAMARGINCALLLISTREQ._serialized_start=12910
  _PROTOOAMARGINCALLLISTREQ._serialized_end=13038
  _PROTOOAMARGINCALLLISTRES._serialized_start=13041
  _PROTOOAMARGINCALLLISTRES._serialized_end=13180
  _PROTOOAMARGINCALLUPDATEREQ._serialized_start=13183
  _PROTOOAMARGINCALLUPDATEREQ._serialized_end=13355
  _PROTOOAMARGINCALLUPDATERES._serialized_start=13357
  _PROTOOAMARGINCALLUPDATERES._serialized_end=13460
  _PROTOOAMARGINCALLUPDATEEVENT._serialized_start=13463
  _PROTOOAMARGINCALLUPDATEEVENT._serialized_end=13639
  _PROTOOAMARGINCALLTRIGGEREVENT._serialized_start=13642
  _PROTOOAMARGINCALLTRIGGEREVENT._serialized_end=13820
  _PROTOOAGETDYNAMICLEVERAGEBYIDREQ._serialized_start=13823
  _PROTOOAGETDYNAMICLEVERAGEBYIDREQ._serialized_end=13983
  _PROTOOAGETDYNAMICLEVERAGEBYIDRES._serialized_start=13986
  _PROTOOAGETDYNAMICLEVERAGEBYIDRES._serialized_end=14169
  _PROTOOADEALLISTBYPOSITIONIDREQ._serialized_start=14172
  _PROTOOADEALLISTBYPOSITIONIDREQ._serialized_end=14378
  _PROTOOADEALLISTBYPOSITIONIDRES._serialized_start=14381
  _PROTOOADEALLISTBYPOSITIONIDRES._serialized_end=14568
  _PROTOOADEALOFFSETLISTREQ._serialized_start=14670
  _PROTOOADEALOFFSETLISTREQ._serialized_end=14814
  _PROTOOADEALOFFSETLISTRES._serialized_start=14817
  _PROTOOADEALOFFSETLISTRES._serialized_end=15023
  _PROTOOAGETPOSITIONUNREALIZEDPNLREQ._serialized_start=15026
  _PROTOOAGETPOSITIONUNREALIZEDPNLREQ._serialized_end=15175
  _PROTOOAGETPOSITIONUNREALIZEDPNLRES._serialized_start=15178
  _PROTOOAGETPOSITIONUNREALIZEDPNLRES._serialized_end=15410
  _PROTOOAORDERDETAILSREQ._serialized_start=15413
  _PROTOOAORDERDETAILSREQ._serialized_end=15553
  _PROTOOAORDERDETAILSRES._serialized_start=15556
  _PROTOOAORDERDETAILSRES._serialized_end=15737
  _PROTOOAORDERLISTBYPOSITIONIDREQ._serialized_start=15740
  _PROTOOAORDERLISTBYPOSITIONIDREQ._serialized_end=15948
  _PROTOOAORDERLISTBYPOSITIONIDRES._serialized_start=15951
  _PROTOOAORDERLISTBYPOSITIONIDRES._serialized_end=16142
  _PROTOOAV1PNLCHANGESUBSCRIBEREQ._serialized_start = 16145
  _PROTOOAV1PNLCHANGESUBSCRIBEREQ._serialized_end = 16286
  _PROTOOAV1PNLCHANGESUBSCRIBERES._serialized_start = 16289
  _PROTOOAV1PNLCHANGESUBSCRIBERES._serialized_end = 16430
  _PROTOOAV1PNLCHANGEUNSUBSCRIBEREQ._serialized_start = 16433
  _PROTOOAV1PNLCHANGEUNSUBSCRIBEREQ._serialized_end = 16579
  _PROTOOAV1PNLCHANGEUNSUBSCRIBERES._serialized_start = 16582
  _PROTOOAV1PNLCHANGEUNSUBSCRIBERES._serialized_end = 16728
# @@protoc_insertion_point(module_scope)
