from urllib.request import urlopen
import json
import pandas as pd
import disaster_type
pd.set_option('display.max_columns', None)

def get_insurance_policy(state):
    try:
        df = disaster_type.get_fima_data(state)
        
        if df['incidentType'].value_counts().idxmax() == 'Fire':
            message = ""
            return message
        
        elif df['incidentType'].value_counts().idxmax() == 'Hurricane':
            message = """
The Best Hurricane Insurance Companies
For most households, the best hurricane insurance coverage is part of the home coverage provided with the best homeowners insurance policies. However, some home insurance providers may not write policies in all states or in areas nearest to the coast of your state. Homeowners closest to the coast or those with high-value homes should consider speaking to an independent agent who can find the coverage you need for your home.


Read Review
COMPARE QUOTES
1. Best Overall: Amica
At this time, Amica does not write home insurance policies in Florida. However, for those further up the East Coast, Amica is a solid choice for homeowners and offers a number of benefits that may cost more with other insurers. In some areas, you may even be able to add earthquake or flood coverage for your home.

Amica’s Platinum Choice policy offers up to 30% more coverage for your home than a standard policy. You’ll also find included extras, like replacement cost coverage for your belongings without a deduction for depreciation, sewer backup coverage and even extended coverage for business property at your home, such as a laptop.

Expect exceptional claim service from Amica, the top-rated company in J.D. Power’s 2018 home insurance customer satisfaction survey. With over 100 years of experience protecting families and an A+ financial rating from A.M. Best, Amica has the staying power you’ll want in a home insurance company.

Read Benzinga’s full Amica Insurance Review


Read Review
CLICK HERE
2. Best for Florida Residents: Kin Insurance
Take a serious look at Kin if you want to save money on home insurance. Kin Insurance curates data and packages policies that fit your needs exactly. The best part? You can insure your home or property in less than 15 minutes, thanks to Kin’s easy and efficient online application. Here’s why you want to take a look:

The more your home can withstand Florida weather, the cheaper your premium will be.
Customer service reps answer your questions right away.
Home insurance policies offer hurricane and wind protection.
Get a custom quote with Kin Insurance and see why this up-to-the-minute insurance company satisfies Florida homeowners all across the Sunshine State.


COMPARE QUOTES
3. PURE Insurance
PURE is a newer insurer with a focus on high-value homes often found in coastal areas.

High-value homes and high-net-worth households have special coverage considerations and PURE has proven its ability to cover the needs of customers in many coastal states like Florida, Georgia, North Carolina, New York, New Jersey, South Carolina, Texas and Maryland.

Expect white-glove claims service and options that aren’t available from many other insurers, like cash settlement (instead of rebuilding) and guaranteed replacement cost coverage. Flood insurance can be added to your policy bundle as well.


Read Review
COMPARE QUOTES
4. State Farm
Financial strength and a wide network of agents are important and State Farm has you covered.

As with other insurers, home insurance may not be available in all areas, but State Farm covers most inland coastal areas and coverage may also be available through affiliated companies so you can take advantage of multi-policy discounts.

Expect prompt claims clearance and knowledgeable agents. Rates can vary by location, insured value and individual rating factors, but State Farm often compares favorably compared to other insurers’ home insurance rates. Flood insurance coverage can be added as a separate policy through agents enrolled in the NFIP-Direct program.

Source: https://www.benzinga.com/money/hurricane-insurance/
"""
            return message
        elif df['incidentType'].value_counts().idxmax() == 'Tornado':
            message = """
Best Overall: Amica
Top-ranked for customer satisfaction in a recent J.D. Power home insurance study, Amica is a top choice if you want comprehensive and affordable coverage for your home. Amica’s Platinum Choice Home policy bundles popular coverage options into an easy-to-understand package.

Dwelling coverage for your home itself provides extended coverage that can protect you against cost overruns. Personal property coverage is offered as replacement cost with select policies, which means your belongings are protected for the full cost of repair or replacement up to your coverage limit.

Homeowners who choose to ensure their vehicles with Amica as well can save up to 15%. Amica also offers the convenient option of purchasing flood insurance to complement your standard home owners insurance coverage.

Amica also tops Benzinga’s lists for the best fire insurance and the best earthquake insurance. Take a look at Benzinga’s full Amica Home Insurance Review.


Farmers
Farmers is actually a worldwide family of companies, which means your Farmers agent may have more coverage options available than some other well-known national insurance brands. This can be especially helpful with difficult-to-insure homes.

Farmers gives you the policy options you need to protect your home against tornado and wind damage. Replacement cost coverage for personal property is available as well as replacement cost coverage for your roof, which can be difficult to find with other insurers.

You’ll also find flexible coverage options available for additional living expenses, which can help cover the cost of temporary housing and other additional living expenses if a covered claim forces you to leave your home temporarily. A claims-free discount and declining deductibles help to keep the overall cost of your policy down if you don’t have a claim.

Farmers Insurance takes top spots in Benzinga’s picks for the best mobile home insurance, the best condo insurance and the best jewelry insurance.



Nationwide
Nationwide has nearly a century of experience insuring families and businesses and is a solid choice for homeowners insurance. Thoughtful policy options make Nationwide a standout when considering home insurance with a focus on potential damage from tornadoes or wind storms.

Nationwide Replacement Cost Plus option can provide an additional 20% above your properties coverage limit if your home needs to be rebuilt due to a covered claim. Nationwide’s Brand New Belongings policy option provides replacement cost coverage for personal property.

Better Roof Replacement, another forward-thinking option available from Nationwide, provides upgraded roofing materials if you have a covered loss that damages your roof. Discounts are also available for newer roofs or based on the type of roof construction.

Source: https://www.benzinga.com/money/a-guide-to-tornado-insurance/
            """
            return message
        
        elif df['incidentType'].value_counts().idxmax() == 'Earthquake':
            message = """
The 7 Best Earthquake Insurance Providers of 2020
<a href='https://www.allstate.com/disaster-help/earthquake.aspx' target="_blank">Allstate</a>: Best Overall
<a href='https://www.statefarm.com/simple-insights/safety/earthquake' target="_blank">State Farm</a>: Best Overall (Runner-Up)
<a href='https://www.amica.com/en/claim-center/storm-center/earthquake.html' target="_blank">Amica Mutual</a>: Best for Added Coverage
<a href='https://www.farmers.com/home/earthquake/' target="_blank">Farmers</a>: Best for Customer Service
<a href='https://www.pureinsurance.com/' target="_blank">PURE Insurance</a>: Best for High-Value Homes
<a href='https://www.amfam.com/insurance/home/earthquake-coverage' target="_blank">American Family Insurance</a>: Best for Bundling for Discounts
<a href='https://www.earthquakeauthority.com/' target="_blank">California Earthquake Authority</a>: Best for California Residents

Source: https://thespruce.com/best-earthquake-insurance-providers-4845289
            """
            return message
        
        else:
            message = """
Fortunately, your area does not seem like it is faces a large threat from natural disasters. However, you should look towards buying home insurance if you have not already done so. These are the best insurance policies and what they each have to offer.

<table class="table --bordered --spacing-xs" style="height: 443px;" width="467">
<tbody>
<tr>
<td style="text-align: center;"><strong>Provider</strong></td>
<td style="text-align: center;"><strong>J.D. Power</strong></td>
<td style="text-align: center;"><strong>AM Best</strong></td>
<td style="text-align: center;"><strong>Consumer Affairs</strong></td>
</tr>
<tr>
<td style="text-align: center;"><strong><a href="https://www.bankrate.com/insurance/companies/amica/" data-linktype="contentInline" data-ctaposition="1">Amica Mutual</a></strong></td>
<td style="text-align: center;">5 out of 5</td>
<td style="text-align: center;">A+</td>
<td style="text-align: center;">Not rated</td>
</tr>
<tr>
<td style="text-align: center;"><strong><a href="https://www.bankrate.com/insurance/companies/allstate/" data-linktype="contentInline" data-ctaposition="2">Allstate</a></strong></td>
<td style="text-align: center;">3 out of 5</td>
<td style="text-align: center;">A+</td>
<td style="text-align: center;"><a href="https://www.consumeraffairs.com/insurance/allstate.htm" target="_blank" rel="noopener" data-linktype="contentInline" data-ctaposition="3">1 star</a></td>
</tr>
<tr>
<td style="text-align: center;"><strong><a href="https://www.bankrate.com/insurance/companies/geico/" data-linktype="contentInline" data-ctaposition="4">Geico</a></strong></td>
<td style="text-align: center;">N/A</td>
<td style="text-align: center;">A++</td>
<td style="text-align: center;"><a href="https://www.consumeraffairs.com/insurance/geico.htm" target="_blank" rel="noopener" data-linktype="contentInline" data-ctaposition="5">2 stars</a></td>
</tr>
<tr>
<td style="text-align: center;"><strong><a href="https://www.bankrate.com/insurance/companies/metlife/" data-linktype="contentInline" data-ctaposition="6">Metlife</a></strong></td>
<td style="text-align: center;">2 out of 5</td>
<td style="text-align: center;">A+</td>
<td style="text-align: center;">3 stars</td>
</tr>
<tr>
<td style="text-align: center;"><strong><a href="https://www.bankrate.com/insurance/companies/usaa/" data-linktype="contentInline" data-ctaposition="7">USAA</a></strong></td>
<td style="text-align: center;">5 out of 5</td>
<td style="text-align: center;">A++</td>
<td style="text-align: center;"><a href="https://www.consumeraffairs.com/insurance/usaa_homeowners.html" target="_blank" rel="noopener" data-linktype="contentInline" data-ctaposition="8">1 star</a></td>
</tr>
<tr>
<td style="text-align: center;"><strong>Chubb</strong></td>
<td style="text-align: center;">2 out of 5</td>
<td style="text-align: center;">A++</td>
<td style="text-align: center;">Not rated</td>
</tr>
</tbody>
</table>

Source: https://www.bankrate.com/insurance/homeowners-insurance/best-home-insurance-companies/
            """
            return message
        
    except Exception as e:
            message = """
Fortunately, your area does not seem like it is faces a large threat from natural disasters. However, you should look towards buying home insurance if you have not already done so. These are the best insurance policies and what they each have to offer.

<table class="table --bordered --spacing-xs" style="height: 443px;" width="467">
<tbody>
<tr>
<td style="text-align: center;"><strong>Provider</strong></td>
<td style="text-align: center;"><strong>J.D. Power</strong></td>
<td style="text-align: center;"><strong>AM Best</strong></td>
<td style="text-align: center;"><strong>Consumer Affairs</strong></td>
</tr>
<tr>
<td style="text-align: center;"><strong><a href="https://www.bankrate.com/insurance/companies/amica/" data-linktype="contentInline" data-ctaposition="1">Amica Mutual</a></strong></td>
<td style="text-align: center;">5 out of 5</td>
<td style="text-align: center;">A+</td>
<td style="text-align: center;">Not rated</td>
</tr>
<tr>
<td style="text-align: center;"><strong><a href="https://www.bankrate.com/insurance/companies/allstate/" data-linktype="contentInline" data-ctaposition="2">Allstate</a></strong></td>
<td style="text-align: center;">3 out of 5</td>
<td style="text-align: center;">A+</td>
<td style="text-align: center;"><a href="https://www.consumeraffairs.com/insurance/allstate.htm" target="_blank" rel="noopener" data-linktype="contentInline" data-ctaposition="3">1 star</a></td>
</tr>
<tr>
<td style="text-align: center;"><strong><a href="https://www.bankrate.com/insurance/companies/geico/" data-linktype="contentInline" data-ctaposition="4">Geico</a></strong></td>
<td style="text-align: center;">N/A</td>
<td style="text-align: center;">A++</td>
<td style="text-align: center;"><a href="https://www.consumeraffairs.com/insurance/geico.htm" target="_blank" rel="noopener" data-linktype="contentInline" data-ctaposition="5">2 stars</a></td>
</tr>
<tr>
<td style="text-align: center;"><strong><a href="https://www.bankrate.com/insurance/companies/metlife/" data-linktype="contentInline" data-ctaposition="6">Metlife</a></strong></td>
<td style="text-align: center;">2 out of 5</td>
<td style="text-align: center;">A+</td>
<td style="text-align: center;">3 stars</td>
</tr>
<tr>
<td style="text-align: center;"><strong><a href="https://www.bankrate.com/insurance/companies/usaa/" data-linktype="contentInline" data-ctaposition="7">USAA</a></strong></td>
<td style="text-align: center;">5 out of 5</td>
<td style="text-align: center;">A++</td>
<td style="text-align: center;"><a href="https://www.consumeraffairs.com/insurance/usaa_homeowners.html" target="_blank" rel="noopener" data-linktype="contentInline" data-ctaposition="8">1 star</a></td>
</tr>
<tr>
<td style="text-align: center;"><strong>Chubb</strong></td>
<td style="text-align: center;">2 out of 5</td>
<td style="text-align: center;">A++</td>
<td style="text-align: center;">Not rated</td>
</tr>
</tbody>
</table>

Source: https://www.bankrate.com/insurance/homeowners-insurance/best-home-insurance-companies/
            """
            return message

state = 'NJ'
get_insurance_policy(state)